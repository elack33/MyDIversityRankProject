from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, render_to_response

from .models import Careers, SurveyResponses


def get_data(request):
    author = request.user
    total_surveys = SurveyResponses.objects.filter(author_id=author).count()
    accounting = (SurveyResponses.objects.filter(author_id=author, career01__career='Accounting').count())
    general_business = SurveyResponses.objects.filter(author_id=author, career01__career='General Business ').count()
    software_development = SurveyResponses.objects.filter(author_id=author, career01__career='Software Development').count()
    admin_clerical = SurveyResponses.objects.filter(author_id=author, career01__career='Admin & Clerical').count()
    general_labor = SurveyResponses.objects.filter(author_id=author, career01__career='General Labor').count()
    pharmaceutical = SurveyResponses.objects.filter(author_id=author, career01__career='Pharmaceutical').count()
    automotive = SurveyResponses.objects.filter(author_id=author, career01__career='Automotive').count()
    government = SurveyResponses.objects.filter(author_id=author, career01__career='Government').count()
    professional_services = SurveyResponses.objects.filter(author_id=author, career01__career='Professional Services').count()
    banking = SurveyResponses.objects.filter(author_id=author, career01__career='Banking').count()
    grocery = SurveyResponses.objects.filter(author_id=author, career01__career='Grocery').count()
    purchasing_procurement = SurveyResponses.objects.filter(author_id=author, career01__career='Purchasing-Procurement').count()
    biotech = SurveyResponses.objects.filter(author_id=author, career01__career='Biotech').count()
    health_care = SurveyResponses.objects.filter(author_id=author, career01__career='Health Care').count()
    qa_quality_control = SurveyResponses.objects.filter(author_id=author, career01__career='QA-Quality Control').count()
    journalism = SurveyResponses.objects.filter(author_id=author, career01__career='Journalism').count()
    hotel_hospitality = SurveyResponses.objects.filter(author_id=author, career01__career='Hotel-Hospitality').count()
    Real_Estate = SurveyResponses.objects.filter(author_id=author, career01__career='Real Estate').count()
    business_development = SurveyResponses.objects.filter(author_id=author, career01__career='Business Development').count()
    human_resources = SurveyResponses.objects.filter(author_id=author, career01__career='Human Resources').count()
    research = SurveyResponses.objects.filter(author_id=author, career01__career='Research').count()
    construction = SurveyResponses.objects.filter(author_id=author, career01__career='Construction').count()
    information_technology = SurveyResponses.objects.filter(author_id=author, career01__career='Information Technology ').count()
    restaurant_food_service = SurveyResponses.objects.filter(author_id=author, career01__career='Restaurant-Food Service').count()
    consultant = SurveyResponses.objects.filter(author_id=author, career01__career='Consultant').count()
    installation_repair = SurveyResponses.objects.filter(author_id=author, career01__career='Installation-Repair ').count()
    retail = SurveyResponses.objects.filter(author_id=author, career01__career='Retail').count()
    customer_service = SurveyResponses.objects.filter(author_id=author, career01__career='Customer Service').count()
    insurance = SurveyResponses.objects.filter(author_id=author, career01__career='Insurance').count()
    sales = SurveyResponses.objects.filter(author_id=author, career01__career='Sales').count()
    design = SurveyResponses.objects.filter(author_id=author, career01__career='Design').count()
    inventory = SurveyResponses.objects.filter(author_id=author, career01__career='Inventory').count()
    science = SurveyResponses.objects.filter(author_id=author, career01__career='Science').count()
    distribution_shipping = SurveyResponses.objects.filter(author_id=author, career01__career='Distribution-Shipping').count()
    legal = SurveyResponses.objects.filter(author_id=author, career01__career='Legal').count()
    skilled_labor_trades = SurveyResponses.objects.filter(author_id=author, career01__career='Skilled Labor-Trades').count()
    education_teaching = SurveyResponses.objects.filter(author_id=author, career01__career='Education-Teaching').count()
    legal_admin = SurveyResponses.objects.filter(author_id=author, career01__career='Legal Admin').count()
    strategy_planning = SurveyResponses.objects.filter(author_id=author, career01__career='Strategy Planning').count()
    engineering = SurveyResponses.objects.filter(author_id=author, career01__career='Engineering').count()
    management = SurveyResponses.objects.filter(author_id=author, career01__career='Management').count()
    supply_chain = SurveyResponses.objects.filter(author_id=author, career01__career='Supply Chain').count()
    entry_level = SurveyResponses.objects.filter(author_id=author, career01__career='Entry Level ').count()
    manufacturing = SurveyResponses.objects.filter(author_id=author, career01__career='Manufacturing').count()
    telecommunications = SurveyResponses.objects.filter(author_id=author, career01__career='Telecommunications').count()
    executive = SurveyResponses.objects.filter(author_id=author, career01__career='Executive').count()
    marketing = SurveyResponses.objects.filter(author_id=author, career01__career='Marketing').count()
    training = SurveyResponses.objects.filter(author_id=author, career01__career='Training').count()
    facilities = SurveyResponses.objects.filter(author_id=author, career01__career='Facilities').count()
    media = SurveyResponses.objects.filter(author_id=author, career01__career='Media').count()
    newspaper = SurveyResponses.objects.filter(author_id=author, career01__career='Newspaper').count()
    transportation = SurveyResponses.objects.filter(author_id=author, career01__career='Transportation').count()
    finance = SurveyResponses.objects.filter(author_id=author, career01__career='Finance').count()
    nonprofit = SurveyResponses.objects.filter(author_id=author, career01__career='Nonprofit').count()
    social_services = SurveyResponses.objects.filter(author_id=author, career01__career='Social Services').count()
    warehouse = SurveyResponses.objects.filter(author_id=author, career01__career='Warehouse').count()
    other = SurveyResponses.objects.filter(author_id=author, career01__career='Other').count()

    return {
        'accounting': accounting,
        'general_business': general_business,
        'software_development': software_development,
        'admin_clerical': admin_clerical,
        'general_labor': general_labor,
        'pharmaceutical': pharmaceutical,
        'automotive': automotive,
        'government': government,
        'professional_services': professional_services,
        'banking': banking,
        'grocery': grocery,
        'purchasing_procurement': purchasing_procurement,
        'biotech': biotech,
        'health_care': health_care,
        'qa_quality_control': qa_quality_control,
        'journalism': journalism,
        'hotel_hospitality': hotel_hospitality,
        'Real_Estate': Real_Estate,
        'business_development': business_development,
        'human_resources': human_resources,
        'research': research,
        'construction': construction,
        'information_technology': information_technology,
        'restaurant_food_service': restaurant_food_service,
        'consultant': consultant,
        'installation_repair': installation_repair,
        'retail': retail,
        'customer_service': customer_service,
        'insurance': insurance,
        'sales': sales,
        'design': design,
        'inventory': inventory,
        'science': science,
        'distribution_shipping': distribution_shipping,
        'legal': legal,
        'skilled_labor_trades': skilled_labor_trades,
        'education_teaching': education_teaching,
        'legal_admin': legal_admin,
        'strategy_planning': strategy_planning,
        'engineering': engineering,
        'management': management,
        'supply_chain': supply_chain,
        'entry_level': entry_level,
        'manufacturing': manufacturing,
        'telecommunications': telecommunications,
        'executive': executive,
        'marketing': marketing,
        'training': training,
        'facilities': facilities,
        'media': media,
        'newspaper': newspaper,
        'transportation': transportation,
        'finance': finance,
        'nonprofit': nonprofit,
        'social_services': social_services,
        'warehouse': warehouse,
        'other': other

    }