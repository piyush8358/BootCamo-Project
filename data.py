# import pandas
import pandas as pd

# List of Tuples
Employees= [('Stuti', 28, 'Varanasi','F',20000, 'Operator','M.TECH', 'Data Manager','2Years','Yes','Completed',12),
			('Athrav', 32, 'Delhi','M', 25000, 'Designer','B.TECH', 'UI Devlopment','7Years','Yes','First Dose',16),
			('Aaditya', 25, 'Mumbai','M', 40000, 'Creator','B.TECH', 'Animation','4Year','None','None',3),
			('Tushar', 34, 'Delhi','M', 35000,'Hr','MBA' ,'Staff','5Years','Yes','Completed',13),
			('Saumya',32 , 'Delhi','F', 40000, 'Manager','MBA' ,'Production','8Years','Yes','First Dose',10),
			('Saumya', 27, 'Mumbai','F', 19000, 'Receptionist', '  Foundation Skill ' ,'Query','3Years','Yes','First Dose',0),
			('Aaditya', 50, 'Dehradun','M', 84000, 'Chairman','M,TECH', 'Board of Director','22Years','yes','Completed',40),
			('Seema', 38, 'Delhi','F', 70000, 'Md','PHD' ,' Board of, Memeber','13Years','Yes','First Dose',23),
            ('Reema', 32, 'Bhopal','F', 20000, 'secretary','B,COM' ,'All details','1Years','None','None',15,),
	        ('Ajay',26,'Up','M',21500,'Analyst','M.TECH','DATA','3Years','Yes', 'First Dose',2),
	        ('Siya',31,'Indore','F',32000,'Developer','B.TECH','Creation','7Years','Yes', 'Completed',5),

      ]

# Create a DataFrame object from list
df = pd.DataFrame(Employees,
				columns =['Name', 'Age',
						'place', 'sex','Salary','Post','Qualifiaction','Department', ' Work Experience ','Vaccinated','Dose Taken','No of Project Done'])
# Show the dataframe
df