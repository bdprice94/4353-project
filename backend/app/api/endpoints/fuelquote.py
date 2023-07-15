Ellalooo
Ellalooo#7095

butterfly — 06/13/2023 8:32 PM
https://buildyourfuture.withgoogle.com/scholarships/google-conference-scholarships
Build your future with Google
We're here to help get you to your future — whether it's business or engineering technology, we got you.
Ellalooo — 06/13/2023 8:32 PM
butterfly — 06/13/2023 8:32 PM
grace hoper confrence and great minds in stem conference
Ellalooo — 06/22/2023 4:44 PM
https://www.youtube.com/watch?v=SqcY0GlETPk&ab_channel=ProgrammingwithMosh
YouTube
Programming with Mosh
React Tutorial for Beginners
Image
butterfly — 06/22/2023 4:45 PM
slayyy ty
Ellalooo — 06/22/2023 4:45 PM
https://react.dev/learn
Quick Start – React
The library for web and native user interfaces
Quick Start – React
butterfly — 06/22/2023 4:45 PM
can we meet sat
imfree all day
Ellalooo — 06/22/2023 4:45 PM
https://www.youtube.com/watch?v=VozPNrt-LfE&amp;ab_channel=Academind
YouTube
Academind
React Native Crash Course | Build a Complete App
Image
Yes of course! I’ll try to be there at 10am!!!
butterfly — 06/25/2023 12:59 PM
import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";
Ellalooo — 06/25/2023 4:17 PM
React.FC = () =>
useState("");
Ellalooo — 06/28/2023 8:16 PM
Hi Cairo! Cnan I hop on a call with you?
Ellalooo
 started a call that lasted 2 minutes.
 — 06/28/2023 8:36 PM
butterfly — 07/02/2023 3:23 PM
Attachment file type: acrobat
UbicompSyllabus2022.pdf
200.97 KB
Ellalooo — 07/02/2023 8:48 PM
Image
ugh
butterfly — 07/03/2023 2:58 PM
yeah im dropping ugh
Ellalooo
 started a call.
 — Today at 7:39 PM
butterfly — Today at 7:46 PM
from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from datetime import date,datetime
import app.models as models
import app.schemas as schemas
Expand
fuelqote.py
2 KB
﻿
from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from datetime import date,datetime
import app.models as models
import app.schemas as schemas
from app.api import deps

router = APIRouter()


@router.post("/fuelquote/{username}",  response_model=schemas.FuelQuote)
async def submit_fuelquote_form(username:str,fuelquote: schemas.FuelQuote, db: Session = Depends(deps.get_session)
):

  user = db.query(models.User).where(models.User.username == fuelquote.username)
  if not user:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")


  fuelquote = models.FuelQuote(username= username, gallons_requested= fuelquote.gallons_requested,delivery_address = fuelquote.delivery_address,delivery_date=fuelquote.delivery_date,suggested_price = fuelquote.suggested_price,total_amount_due = fuelquote.total_amount_due)
  db.add(fuelquote)
  db.commit()
  
  return {"username": username, "gallons_requested":fuelquote.gallons_requested, "delivery_address":fuelquote.delivery_address, "delivery_date":fuelquote.delivery_date, "suggested_price": fuelquote.suggested_price, "total_amount_due":fuelquote.total_amount_due}
  
@router.get("/getfuelquote/{username}", response_model=List[schemas.FuelQuote])
async def get_fuelquotes_by_user(username: str,db: Session = Depends(deps.get_session)
):
  fuelquote = db.query(models.FuelQuote).filter(models.FuelQuote.username == username).all()
  return fuelquote
fuelqote.py
2 KB