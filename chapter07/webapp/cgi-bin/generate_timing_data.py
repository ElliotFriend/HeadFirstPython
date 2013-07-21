import cgi
import athletemodel
import yate

#import cgitb
#cgitb.enable()

athletes = athletemodel.get_from_store()

form_data = cgi.FieldStorage()
athlete_name = form_data['which_athlete'].value

print(yate.start_response())
print(yate.include_header("Coach Kelly's TimingData"))
print(yate.header("Timing data for " + athlete_name + ", DOB; "
                  + athletes[athlete_name].dob))
print(yate.para("The top times for " + athlete_name + " are:"))
print(yate.u_list(athletes[athlete_name].top3))

print(yate.include_footer({"Home" : "/index.html",
                          "Select Another Athlete" : "generate_list.py"}))
