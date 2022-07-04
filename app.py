# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 21:23:04 2022

@author: harsh
"""


import numpy as np
import pickle
import streamlit as st



#loading the saved model
mdl=pickle.load(open(r"RFR_trained.pkl",'rb'))

# creating a function for prediction

def cost_estimation(input_data):
    #changing the input data to numpy array
    inp_dat_np=np.asarray(input_data)
    
    #reshaping the array as we are predicting for one instance
    inp_data=inp_dat_np.reshape(1,-1)
    
    pred=mdl.predict(inp_data)
    print(pred)
    
    return pred
    
def main():
    # giving a title
    st.title("Software Cost Estimation")
    
    #getting input data from the user
    
    org_prof = st.selectbox('Organisation Profile',('Banking', 'Billing', 'Telecommunication'))
    b_dom = st.selectbox('Business Domain',('Billing', 'Call Centre Solution', 'Client & Account Management','Data Warehouse & BI','Finance & Risk','Front Office Solution','Internet & Mobile','Mortgages','Organizations','Payments','Savings & Loans'))
    dev_method = st.selectbox('Development Method',('Plan Driven(Waterfall)', 'RUP', 'Scrum(Agile)'))
    dev_class = st.selectbox('Developemnt Class',('Conversion(<5%)', 'Minor Enhancement(5%-25% new)', 'Major Enhancement(25%-75% new)','New Development'))
    
    func_size = st.text_input("Function Size")
    act_dur = st.text_input("Estimated Duration")
    
    release = st.selectbox('Release Based Working',('Yes','No'))
    once_only_proj = st.selectbox('Once Only Project',('Yes','No'))
    multi_app = st.selectbox('Multiple Application Release',('Yes','No'))
    phased_proj = st.selectbox('Phased Project',('Yes','No'))
    doa = st.selectbox('Dependencies with other applications',('Yes','No'))
    single_app = st.selectbox('Single Application',('Yes','No'))
    mig_proj = st.selectbox('Migration Project',('Yes','No'))
    prob_ext = st.selectbox('Problem with External Supplier',('Yes','No'))
    sec_proj = st.selectbox('Security related Project',('Yes','No'))
    pack_shelf = st.selectbox('Package of the Shelf',('Yes','No'))
    pack_cust = st.selectbox('Package with Customization',('Yes','No'))
    steady_hb = st.selectbox('Steady Heartbeat',('Yes','No'))
    mtc = st.selectbox('Many team changes unexperienced team',('Yes','No'))
    leg = st.selectbox('Legacy Application',('Yes','No'))
    tech_driven = st.selectbox('Technology Driven Project',('Yes','No')) 
    rr = st.selectbox('Rules and Regulation Driven Project',('Yes','No'))
    bdp = st.selectbox('Business Driven Project',('Yes','No'))
    ppc = st.selectbox('Pilot or Proof Concept',('Yes','No'))
    
    
    
    
    lst=[release,once_only_proj,multi_app,phased_proj,doa,single_app,mig_proj,prob_ext,sec_proj,pack_shelf,pack_cust,steady_hb,mtc,leg,tech_driven,rr,bdp,ppc]
    
    if(release=='Yes'):
        g1=1
    else:
        g1=0
    
    if(once_only_proj=='Yes'):
        g2=1
    else:
        g2=0
        
    if(multi_app=='Yes'):
        g3=1
    else:
        g3=0
    
    if(phased_proj=='Yes'):
        g4=1
    else:
        g4=0
    
    if(doa=='Yes'):
        g5=1
    else:
        g5=0
    
    if(single_app=='Yes'):
        g6=1
    else:
        g6=0
    
    if(mig_proj=='Yes'):
        g7=1
    else:
        g7=0
    
    if(prob_ext=='Yes'):
        g8=1
    else:
        g8=0
    
    if(sec_proj=='Yes'):
        g9=1
    else:
        g9=0
    
    if(pack_shelf=='Yes'):
        g10=1
    else:
        g10=0
    
    if(pack_cust=='Yes'):
        g11=1
    else:
        g11=0
        
    if(steady_hb=='Yes'):
        g12=1
    else:
        g12=0
        
    if(mtc=='Yes'):
        g13=1
    else:
        g13=0
    
    if(leg=='Yes'):
        g14=1
    else:
        g14=0
        
    if(tech_driven=='Yes'):
        g15=1
    else:
        g15=0
        
    if(rr=='Yes'):
        g16=1
    else:
        g16=0
        
    if(bdp=='Yes'):
        g17=1
    else:
        g17=0
        
    if(ppc=='Yes'):
        g18=1
    else:
        g18=0
    
    if(org_prof == 'Banking'):
        o1=1
        o2=0
        o3=0
    elif(org_prof == 'Billing'):
        o1=0
        o2=1
        o3=0
    elif(org_prof == 'Telecommunication'):
        o1=0
        o2=0
        o3=1
    
    if(b_dom == 'Billing'):
        b1=1
        b2=0
        b3=0
        b4=0
        b5=0
        b6=0
        b7=0
        b8=0
        b9=0
        b10=0
        b11=0
    elif(b_dom == 'Call Centre Solution'):
        b1=0
        b2=1
        b3=0
        b4=0
        b5=0
        b6=0
        b7=0
        b8=0
        b9=0
        b10=0
        b11=0
    elif(b_dom == 'Client & Account Management'):
        b1=0
        b2=0
        b3=1
        b4=0
        b5=0
        b6=0
        b7=0
        b8=0
        b9=0
        b10=0
        b11=0
    elif(b_dom == 'Data Warehouse & BI'):
        b1=0
        b2=0
        b3=0
        b4=1
        b5=0
        b6=0
        b7=0
        b8=0
        b9=0
        b10=0
        b11=0
    elif(b_dom == 'Finance & Risk'):
        b1=0
        b2=0
        b3=0
        b4=0
        b5=1
        b6=0
        b7=0
        b8=0
        b9=0
        b10=0
        b11=0
    elif(b_dom == 'Front Office Solution'):
        b1=0
        b2=0
        b3=0
        b4=0
        b5=0
        b6=1
        b7=0
        b8=0
        b9=0
        b10=0
        b11=0
    elif(b_dom == 'Internet & Mobile'):
        b1=0
        b2=0
        b3=0
        b4=0
        b5=0
        b6=0
        b7=1
        b8=0
        b9=0
        b10=0
        b11=0
    elif(b_dom == 'Mortgages'):
        b1=0
        b2=0
        b3=0
        b4=0
        b5=0
        b6=0
        b7=0
        b8=1
        b9=0
        b10=0
        b11=0
    elif(b_dom == 'Organizations'):
        b1=0
        b2=0
        b3=0
        b4=0
        b5=0
        b6=0
        b7=0
        b8=0
        b9=1
        b10=0
        b11=0
    elif(b_dom == 'Payments'):
        b1=0
        b2=0
        b3=0
        b4=0
        b5=0
        b6=0
        b7=0
        b8=0
        b9=0
        b10=1
        b11=0
    elif(b_dom == 'Savings & Loans'):
        b1=0
        b2=0
        b3=0
        b4=0
        b5=0
        b6=0
        b7=0
        b8=0
        b9=0
        b10=0
        b11=1
        
    if(dev_method == 'Plan Driven(Waterfall)'):
        d1=1
        d2=0
        d3=0
    elif(dev_method == 'RUP'):
        d1=0
        d2=1
        d3=0
    elif(dev_method == 'Scrum(Agile)'):
        d1=0
        d2=0
        d3=1

    if(dev_class == 'Conversion(<5%)'):
        c1=1
        c2=0
        c3=0
        c4=0
    elif(dev_class == 'Major Enhancement(25%-75% new)'):
        c1=0
        c2=1
        c3=0
        c4=0
    elif(dev_class == 'Minor Enhancement(5%-25% new)'):
        c1=0
        c2=0
        c3=1
        c4=0
    elif(dev_class == 'New Development'):
        c1=0
        c2=0
        c3=0
        c4=1
        
    #creating button for prediction
    diagnosis=''
    if st.button("Software Cost"):
        diagnosis = cost_estimation([func_size,act_dur,g1,g2,g3,g4,g5,g6,g7,g8,g9,g10,g11,g12,g13,g14,g15,g16,g17,g18,o1,o2,o3,b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,d1,d2,d3,c1,c2,c3,c4])
    
    st.success(diagnosis)
    

if __name__ == '__main__':
    main()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
