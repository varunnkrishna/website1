from django.shortcuts import render, redirect
from .models import submit_form_ml
from validate_email import validate_email
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, 'index.html')

def submit_form(request): 
    if request.method == 'POST':
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        email_address = request.POST["email_address"]
        message = request.POST["message"]

        is_valid = validate_email(email_address)
 
        if is_valid:
            submit_info = submit_form_ml(first_name= first_name, last_name= last_name, email_address=email_address, message= message)
            submit_info.save()
            print("the form is subitted")
            return render(request,'thankyou.html' )
        else:
            # return render(request, 'error.html')
            messages.info(request, "Your email is not valid, please enter again")
            return redirect("/")

    return render(request, 'index.html')

  
        


    
       

    
    
        




    

    
   
    


        

    




    
    