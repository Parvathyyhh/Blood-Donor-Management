from mysql import connector
from datetime import datetime

class BloodDonorManager:
    def __init__(self):
        self.connection=connector.connect(
            host="localhost",
            user="root",
            password="Qwert@12345",
            database="blood_db"
        )
        print("Connected Successfully..!")

    def get_object(self,id=None):
        try:
            self.cursor=self.connection.cursor()
            query="select * from donor where id=%s"
            values=(id,)           
            self.cursor.execute(query,values)
            record=self.cursor.fetchone()
            return record
        except Exception as e:
            print(e)
    
    def post(self,**kwargs):
        try:
            self.cursor=self.connection.cursor()
            query="insert into donor(name,blood_group,phone,city,last_donation) values(%s,%s,%s,%s,%s)"
            values=[v for v in kwargs.values()]
            self.cursor.execute(query,values)
            self.connection.commit()
            print("Data inserted successfully..!")
        except Exception as e:
            print(e)

    def get(self):
        try:
            self.cursor = self.connection.cursor()
            query = "select * from donor"
            self.cursor.execute(query)
            records = self.cursor.fetchall()
            return records
        except Exception as e:
           print(e)
    def retrieve(self,id=None):
        try:
            record=self.get_object(id=id)
            if record==None:
                print("No donors found..!")
            print(record)
        except Exception as e:
            print(e)

    def delete(self,id=None):
        try:
            record=self.get_object(id=id)
            if record!=None:
                query="delete from donor where id=%s"
                self.cursor.execute(query,(id,))
                self.connection.commit()
                print("Donor deleted Successfully..!")
            else:
                print("No donors found..!")
        except Exception as e:
            print(e)

    def put(self,id=None,**kwargs):
        try:
            record=self.get_object(id=id)
            if record!=None:
                self.cursor=self.connection.cursor()
                placeholder= ""
                for k in kwargs.keys():
                    placeholder += k + "=%s, "
                placeholder = placeholder.rstrip(", ")
                query=f"update donor set {placeholder} where id=%s"
                values=[v for v in kwargs.values()]
                values.append(id)
                self.cursor.execute(query,values)
                self.connection.commit()
                return True, "Donor Updated Successfully..!"
            else:
                return False, "No donor found..!"
        except Exception as e:
            print(e)

donor_instance=BloodDonorManager()
donor_instance.post(
    name="Anu",
    blood_group="O+",
    phone="9806850110",
    city="Kochi",
    last_donation=datetime.today()
)
donor_instance.get()
donor_instance.retrieve(id=1)
donor_instance.delete(id=7)
donor_instance.put(id=1,name="Anu",blood_group="O-",phone="9806850110",city="Kochi",last_donation=datetime.today())
self.connection.close()