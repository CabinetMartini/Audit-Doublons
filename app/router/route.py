from fastapi import APIRouter, UploadFile, File, HTTPException  # type: ignore
from fastapi.responses import FileResponse
from fastapi.background import BackgroundTasks
import logging
import tempfile
import os
from app.internal.core.FEC import FEC

logger = logging.getLogger()

route = APIRouter()

@route.post("/recherche", status_code=200)
async def recherche(
    background_tasks: BackgroundTasks,
    Fec: UploadFile = File(...)
):
    tmp_input_path = None
    tmp_output_path = None
    try:
        # Sauvegarde du fichier uploadé
        with tempfile.NamedTemporaryFile(delete=False, suffix='.txt') as tmp_file:
            content = await Fec.read()
            tmp_file.write(content)
            tmp_input_path = tmp_file.name

        # Traitement FEC
        tmp_output_path = tmp_input_path.replace('.txt', '_result.xlsx')
        fec = FEC(tmp_input_path, original_filename=Fec.filename or "")
        fec.run(output_path=tmp_output_path)

        background_tasks.add_task(os.remove, tmp_output_path)
        return FileResponse(
            path=tmp_output_path,
            media_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
            filename=f"Recherche_Doublons_{fec.group_name}.xlsx",
            background=background_tasks
        )

    except Exception as e:
        logger.error(f"Erreur lors du traitement du fichier FEC: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Erreur lors du traitement du fichier FEC: {str(e)}")

    finally:
        if tmp_input_path and os.path.exists(tmp_input_path):
            os.remove(tmp_input_path)