from fastapi import APIRouter, Depends, HTTPException, BackgroundTasks
from app.background.remainder_mail import bg_send_task_reminders


router = APIRouter()



@router.get("/")
async def send_task_reminders( background_tasks: BackgroundTasks):
    
    background_tasks.add_task(bg_send_task_reminders)
    return {"message": "Task reminders sent successfully"}
