class student:
    #class variables
    grade=10
    name="Chahat"

    def wishes(self):
        print("hi I am a Student")

    def intro(self):
        print("i am",self.name)
        print("i study in grade",self.grade)

st=student()
st.wishes()
st.intro()