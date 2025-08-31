# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 10:59:11 2025

@author: affan
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu

#loading the saved model
diabetes_model=pickle.load(open("diabetes_model.sav",'rb'))
heart_disease_model=pickle.load(open("heart_disease_model.sav",'rb'))
parkinsons_model=pickle.load(open("parkinsons_model.sav",'rb'))




#side bar for navigation
with st.sidebar:
    selected=option_menu('Multiple disease prediction system ',
                         
                         ['Dibetes Prediction','Heart disease Prediction','Parkinson prediction'],
                         
                         icons=['activity','heart','person'],
                         
                         default_index=0)  # index 0 means  menu me selected index 0th wala hi dikhe ga means Dibetes Prediction khulega
                                            #if index 1 then selscted index 1st wala dekhega meansa heart disease predicrion khulega
    
    
#diabetes prediction
if(selected=='Dibetes Prediction'):
    #page title
    st.title('Diabetes prediction')
    
    
    # getting the input data from user 
    #column for input feild 
    col1,col2,col3=st.columns(3)
    
    with col1:
        Pregnancies=st.text_input('Number of Pregnancies')
    with col2:
        Glucose=st.text_input('Glucose level')
    with col3:
        BloodPressure=st.text_input('BloodPressure value')
    with col1:
        SkinThickness=st.text_input('SkinThickness value')
    with col2:
        Insulin=st.text_input('Insulin level')
    with col3:
        BMI=st.text_input('BMI value')
    with col1:
        DiabetesPedigreeFunction=st.text_input('DiabetesPedigreeFunction value')
    with col2:
        Age=st.text_input('Age of the person')
    
    
    #code for prediction
    diab_dignosis=''
    #creating  a butten
    if st.button("Diabetes test result"):
        diab_predction=diabetes_model.predict([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]])
        
        if(diab_predction[0]==1):
            diab_dignosis='The person is Diabetic'
        else:
            diab_dignosis='The person is not Diabetic'
            
    st.success(diab_dignosis)
    
    
    
    
if(selected=='Heart disease Prediction'):
    #page title
    st.title('Heart disease Prediction')
    
    
    # getting the input data from user 
    #column for input feild 
    col1,col2,col3=st.columns(3)
    
    with col1:
        age=st.text_input('Age of the person')
    with col2:
        sex=st.text_input('sex')
    with col3:
        cp=st.text_input('chest pain type')
    with col1:
        trestbps=st.text_input('resting blood presure')
    with col2:
        chol=st.text_input('serum cholestrole in mg/dl')
    with col3:
        fbs=st.text_input('fasting blood sugar > 120mg/dl')
    with col1:
        restecg=st.text_input('resting electrocardiographic results')
    with col2:
        thalach=st.text_input('maximum heart rate achieved')
    with col3:
         exang=st.text_input('exercise induced angina')
    with col1:
        oldpeak=st.text_input('oldpeak = ST depression induced by exercise relative to rest')
    with col2:
        slope=st.text_input('the slope of the peak exercise ST segment')
    with col3:
        ca=st.text_input('number of major vessels (0-3) colored by flourosopy')
    with col1:
        thal=st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')
    
    
    #code for prediction
    heart_dignosis=''
    #creating  a butten
    if st.button("Heart Disease test result"):
        #heart_predction=heart_disease_model.predict([[age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]])
        heart_predction = heart_disease_model.predict([[int(age), int(sex), int(cp), int(trestbps),
                                                         int(chol), int(fbs), int(restecg), int(thalach),
                                                         int(exang), float(oldpeak), int(slope), int(ca), int(thal)]])
        
        if(heart_predction[0]==1):
            heart_dignosis='The person have heart disease'
        else:
            heart_dignosis='The person heart is healthy'
            
    st.success(heart_dignosis)
    

if(selected=='Parkinson prediction'):
    #page title
    st.title('Parkinson prediction')
    
    
    # getting the input data from user 
    #column for input feild 
    col1,col2,col3,col4,col5=st.columns(5)
    
    with col1:
        MDVP_Fo_Hz=st.text_input(' Average vocal fundamental frequency')
    with col2:
        MDVP_Fhi_Hz=st.text_input('Maximum vocal fundamental frequency')
    with col3:
        MDVP_Flo_Hz=st.text_input(' Minimum vocal fundamental frequency')
    with col4:
        MDVP_Jitter=st.text_input('MDVP:Jitter(%)')
    with col5:
        MDVP_Jitter_Abs=st.text_input('MDVP:Jitter(Abs)')
    with col1:
        MDVP_RAP=st.text_input('MDVP:RAP')
    with col2:
        MDVP_PPQ=st.text_input('MDVP:PPQ')
    with col3:
        Jitter_DDP=st.text_input('Jitter:DDP')
    with col4:
        MDVP_Shimmer=st.text_input('MDVP:Shimmer')
    with col5:
        MDVP_Shimmer_dB=st.text_input('MDVP:Shimmer(dB)')
    with col1:
        Shimmer_APQ3=st.text_input('Shimmer:APQ3')
    with col2:
        Shimmer_APQ5=st.text_input('Shimmer:APQ5')
    with col3:
        MDVP_APQ=st.text_input('MDVP:APQ')
    with col4:
        Shimmer_DDA=st.text_input('Shimmer:DDA')
    with col5:
        NHR=st.text_input('NHR')
    with col1:
        HNR=st.text_input('HNR')
    with col2:
        RPDE=st.text_input('RPDE')
    with col3:
        DFA=st.text_input('DFA')
    with col4:
        spread1=st.text_input('spread1')
    with col5:
        spread2=st.text_input('spread2')
    with col1:
        D2=st.text_input('D2')
    with col2:
        PPE=st.text_input('PPE')

                
    
    #code for prediction
    Parkinson_dignosis=''
    #creating  a butten
    if st.button("parkinson test result"):
        #Parkinson_predction=parkinsons_model.predict([[MDVP_Fo_Hz,MDVP_Fhi_Hz, MDVP_Flo_Hz,MDVP_Jitter,MDVP_Jitter_Abs,MDVP_RAP,MDVP_PPQ,Jitter_DDP,MDVP_Shimmer_dB,Shimmer_APQ3,MDVP_Shimmer,Shimmer_APQ5,MDVP_APQ,Shimmer_DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]])
        Parkinson_predction = parkinsons_model.predict([[float(MDVP_Fo_Hz), float(MDVP_Fhi_Hz), float(MDVP_Flo_Hz),
                                                  float(MDVP_Jitter), float(MDVP_Jitter_Abs), float(MDVP_RAP),
                                                  float(MDVP_PPQ), float(Jitter_DDP), float(MDVP_Shimmer),
                                                  float(MDVP_Shimmer_dB), float(Shimmer_APQ3), float(Shimmer_APQ5),
                                                  float(MDVP_APQ), float(Shimmer_DDA), float(NHR), float(HNR),
                                                  float(RPDE), float(DFA), float(spread1), float(spread2),
                                                  float(D2), float(PPE)]])

        
        if( Parkinson_predction[0]==1):
            Parkinson_dignosis='The person have Parkinson disease'
        else:
            Parkinson_dignosis='The person have not Parkinson disease'
            
    st.success(Parkinson_dignosis)
    

