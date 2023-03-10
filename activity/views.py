from django.shortcuts import render
from django.http import HttpResponse

def CCMS_Mission(request):
    return HttpResponse("The College of Computing and Multimedia Studies shall produce competent and innovative professionals or Technopreneurs in the Information and Communication Technology (ICT) industry adequately prepared in the practice of their profession supportive of national development goals and standards of global excellence.")

def CCMS_Vision(request):
    return HttpResponse("The College of Computing and Multimedia Studies shall be a center of excellence in delivering Computing and Multimedia education.")

def CCMS_Objective(request):
    return HttpResponse("1. Be employed and demonstrate professionalism, competence and passion in solving contemporary computing problems by developing or utilizing innovative IT solutions; \n 2. Embark in lifelong learning or research to attune to the continuous innovation in the IT industry in order to adapt to the changing demands of the global market; and \n 3. Exhibit leadership and teamwork, and commitment to their respective local or global organizations.")
