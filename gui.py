import streamlit as st
from donorView import BloodDonorManager

donor_instance=BloodDonorManager()
blood_groups=["A+","A-","B+","B-","AB+","AB-","O+","O-"]
tab1,tab2,tab3,tab4=st.tabs(["Add Donor","View Donors","Update Details","Delete Donor"])

with tab1:
    st.header("Add New Donors..!")
    name=st.text_input("Enter Donor Name")
    blood_group=st.selectbox("Select Blood Group",["A+","A-","B+","B-","AB+","AB-","O+","O-"])
    phone=st.text_input("Enter Donor Phone Number")
    city=st.text_input("Enter Donor City")
    last_donation=st.date_input("Enter Last Donation date")
    if st.button("Submit"):
        donor_instance.post(name=name,blood_group=blood_group,phone=phone,city=city,last_donation=last_donation)
        st.success("Donor added Successfully..!")

with tab2:
    st.header("View Blood Donor Details..!")
    records=donor_instance.get()
    print("______________")
    print(records)
    if records:
        st.table(records)
    else:
        st.warning("No donor found..!")
with tab3:
    st.title("Update Donor Details")
    records=donor_instance.get()
    if records:
        donor_ids=[r[0] for r in records]    
        id=st.selectbox("Select Donor id",donor_ids,key="update_id")
        record=donor_instance.get_object(id=id)
        name=st.text_input("Enter name",value=record[1])
        phone=st.text_input("Enter mobile number",value=record[3])
        blood_group=st.selectbox("Select your blood group",blood_groups,index=blood_groups.index(record[2]),key="update_group")
        city=st.text_input("Enter your place",value=record[4])               
        last_donation=st.date_input("Enter last donation date",value=record[5])
        if st.button("Update"):
            status,message=donor_instance.put(id=id,
                                              name=name,
                                              phone=phone,                                     
                                              blood_group=blood_group,
                                              city=city,
                                              last_donation=last_donation)
 
            if status:
                st.success(message)
            else:
                st.error(message)
        else:
            st.warning("No donor found..!")
    
    
    