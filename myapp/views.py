from django.shortcuts import render
import os
import joblib
import pandas as pd
from . models import History 

path=os.path.dirname(__file__) # Provide root path of myapp
model=joblib.load(open(os.path.join(path,'best_model.pkl'),'rb'))
label_encoder=joblib.load(open(os.path.join(path,'label_encoder.pkl'),'rb'))

# Create your views here.
def index(req):
    return render(req,"index.html")
def prediction(req):
    if req.method=='POST':
        fever=req.POST['fever']
        headache=req.POST['headache']
        nausea=req.POST['nausea']
        vomiting=req.POST['vomiting']
        fatigue=req.POST['fatigue']
        joint_pain=req.POST['joint_pain']
        skin_rash=req.POST['skin_rash']
        cough=req.POST['cough']
        weight_loss=req.POST['weight_loss']
        yellow_eyes=req.POST['yellow_eyes']
        symptoms=['fever','headache','nausea','vomiting','fatigue','joint_pain','skin_rash','cough','weight_loss','yellow_eyes']
        user_input=[fever,headache,nausea,vomiting,fatigue,joint_pain,skin_rash,cough,weight_loss,yellow_eyes]
        input_df=pd.DataFrame([user_input],columns=symptoms)
        result=model.predict(input_df)[0]
        res=label_encoder.inverse_transform([result])[0]
        #ORM (Object Relationship Mapping)
        his=History(fever=fever, headache=headache, nausea=nausea, vomiting=vomiting, fatigue=fatigue, joint_pain=joint_pain, skin_rash=skin_rash, cough=cough, weight_loss=weight_loss, yellow_eyes=yellow_eyes, res=res)
        his.save()
        return render(req,"prediction.html",{"res":res})
    return render(req,"prediction.html")
def history(req):
    his=History.objects.all() # select * from history
    return render(req,"history.html",{"his":his})