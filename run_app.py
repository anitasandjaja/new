from flask import Flask, render_template, url_for, request, send_from_directory
import numpy as np
import pandas as pd
import folium
import joblib

app = Flask(__name__)
# scaler = joblib.load("scale data") # load scaler
# model = joblib.load("model_svc_tuned")

@app.route("/")
@app.route('/index')
def index():
    return render_template("master.html")

@app.route("/go", methods=["POST", "GET"])
def go():

    myform = request.form

    age = int(myform.getlist('age')[0])
    months = int(myform.getlist('months')[0])
    policy_deduct =int(myform.getlist('policy_deduct')[0])
    policy_annual = float(myform.getlist('policy_annual')[0])
    umbrella_limit = int(myform.getlist('umbrella_limit')[0])
    capital_gains = int(myform.getlist('capital_gains')[0])
    capital_loss = int(myform.getlist('capital_loss')[0])
    number_vehicle = int(myform.getlist('number_vehicle')[0])
    body = int(myform.getlist('body')[0])
    witnesses = int(myform.getlist('witnesses')[0])
    total_claim_amount = int(myform.getlist('total_claim_amount')[0])
    
    arlington = int(myform.getlist('incident_city')[0] == 'arlington')
    columbus = int(myform.getlist('incident_city')[0] == 'columbus')
    hillsdale = int(myform.getlist('incident_city')[0] == 'hillsdale')
    northbend = int(myform.getlist('incident_city')[0] == 'northdbend')
    northbrook = int(myform.getlist('incident_city')[0] == 'northbrook')
    riverwood = int(myform.getlist('incident_city')[0] == 'riverwood')
    springfield = int(myform.getlist('incident_city')[0] == 'springfield')


    incident_type_multivehicle_collision = int(myform.getlist('incident_type')[0] == 'multivehicle_collision')
    incident_type_parked_car = int(myform.getlist('incident_type')[0] == 'parked_car')
    incident_type_single_vehicle = int(myform.getlist('incident_type')[0] == 'single_vehicle_collision')
    incident_type_vehicle_theft = int(myform.getlist('incident_type')[0] == 'vehicle_theft')
    

    associate = int(myform.getlist('education_level')[0] == 'associate')
    college = int(myform.getlist('education_level')[0] == 'college')
    highschool = int(myform.getlist('education_level')[0] == 'highschool')
    jd = int(myform.getlist('education_level')[0] == 'jd')
    md = int(myform.getlist('education_level')[0] == 'md')
    masters = int(myform.getlist('education_level')[0] == 'masters')
    phd = int(myform.getlist('education_level')[0] == 'phd')

    
    insured_occupation_adm_clerical = int(myform.getlist('insured_occupation')[0]== 'insured_occupation_adm-clerical')
    insured_occupation_armed_forces =int(myform.getlist('insured_occupation')[0]== 'insured_occupation_armed-forces')
    insured_occupation_craft_repair = int(myform.getlist('insured_occupation')[0]== 'insured_occupation_craft-repair')
    insured_occupation_exec_managerial = int(myform.getlist('insured_occupation')[0]== 'insured_occupation_exec-managerial')
    insured_occupation_farming_fishing = int(myform.getlist('insured_occupation')[0]== 'insured_occupation_farming-fishing')
    insured_occupation_handlers_cleaners = int(myform.getlist('insured_occupation')[0]== 'insured_occupation_handlers-cleaners')
    insured_occupation_machine_op_inspct= int(myform.getlist('insured_occupation')[0]== 'insured_occupation_machine-op-inspct')
    insured_occupation_other_service = int(myform.getlist('insured_occupation')[0]== 'insured_occupation_other-service')
    insured_occupation_priv_house_service = int(myform.getlist('insured_occupation')[0]== 'insured_occupation_priv-house-service')
    insured_occupation_prof_specialty = int(myform.getlist('insured_occupation')[0]== 'insured_occupation_prof-specialty')
    insured_occupation_protective_serv = int(myform.getlist('insured_occupation')[0]== 'insured_occupation_protective-serv')
    insured_occupation_sales = int(myform.getlist('insured_occupation')[0]== 'insured_occupation_sales')
    insured_occupation_tech_support = int(myform.getlist('insured_occupation')[0]== 'insured_occupation_tech-support')
    insured_occupation_transport_moving = int(myform.getlist('insured_occupation')[0]== 'insured_occupation_transport-moving')

    basejumping = int(myform.getlist('insured_hobbies')[0] == 'insured_hobbies_base-jumping')
    basketball  = int(myform.getlist('insured_hobbies')[0] == 'insured_hobbies_basketball')
    boardgames = int(myform.getlist('insured_hobbies')[0] == 'insured_hobbies_board-games')
    bungiejumping = int(myform.getlist('insured_hobbies')[0] == 'insured_hobbies_bungie-jumping')
    camping = int(myform.getlist('insured_hobbies')[0] == 'insured_hobbies_camping')
    chess = int(myform.getlist('insured_hobbies')[0] == 'insured_hobbies_chess')
    crossfit = int(myform.getlist('insured_hobbies')[0] == 'insured_hobbies_cross-fit')
    dancing = int(myform.getlist('insured_hobbies')[0] == 'insured_hobbies_dancing')
    exercise = int(myform.getlist('insured_hobbies')[0] == 'insured_hobbies_exercise')
    golf = int(myform.getlist('insured_hobbies')[0] == 'insured_hobbies_golf')
    hiking = int(myform.getlist('insured_hobbies')[0] == 'insured_hobbies_hiking')
    kayaking = int(myform.getlist('insured_hobbies')[0] == 'insured_hobbies_kayaking')
    movies = int(myform.getlist('insured_hobbies')[0] == 'insured_hobbies_movies')
    paintball = int(myform.getlist('insured_hobbies')[0] == 'insured_hobbies_paintball')
    polo = int(myform.getlist('insured_hobbies')[0] == 'insured_hobbies_polo')
    reading = int(myform.getlist('insured_hobbies')[0] == 'insured_hobbies_reading')
    skydiving = int(myform.getlist('insured_hobbies')[0] == 'insured_hobbies_skydiving')
    sleeping = int(myform.getlist('insured_hobbies')[0] == 'insured_hobbies_sleeping')
    videogames = int(myform.getlist('insured_hobbies')[0] == 'insured_hobbies_video-games')
    yachting = int(myform.getlist('insured_hobbies')[0] == 'insured_hobbies_yachting')

    property_damage = myform.getlist('property_damage')[0]
  
    stateNC = int(myform.getlist('incident_state')[0] == 'stateNC')
    stateNY = int(myform.getlist('incident_state')[0] == 'stateNY')
    stateOH = int(myform.getlist('incident_state')[0] == 'stateOH')
    statePA = int(myform.getlist('incident_state')[0] == 'statePA')
    stateSC = int(myform.getlist('incident_state')[0] == 'stateSC')
    stateVA = int(myform.getlist('incident_state')[0] == 'stateVA')
    stateWV = int(myform.getlist('incident_state')[0] == 'stateWV')


    accura = int(myform.getlist('auto_make')[0] == 'accura')
    audi = int(myform.getlist('auto_make')[0] == 'audi')
    bmw = int(myform.getlist('auto_make')[0] == 'bmw')
    chev = int(myform.getlist('auto_make')[0] == 'chev')
    dodge = int(myform.getlist('auto_make')[0] == 'dodge')
    ford = int(myform.getlist('auto_make')[0] == 'ford')
    honda = int(myform.getlist('auto_make')[0] == 'honda')
    jeep = int(myform.getlist('auto_make')[0] == 'jeep')
    mercy = int(myform.getlist('auto_make')[0] == 'mercy')
    nissan = int(myform.getlist('auto_make')[0] == 'nissan')
    saab= int(myform.getlist('auto_make')[0] == 'saab')
    suburu = int(myform.getlist('auto_make')[0] == 'suburu')
    toyota = int(myform.getlist('auto_make')[0] == 'toyota')
    volks = int(myform.getlist('auto_make')[0] == 'volks')

    police_report = myform.getlist('police_report_available')[0]

    insured_sex = myform.getlist('insured_sex')[0]

    incident_severity_major_damage = int(myform.getlist('incident_severity')[0] == 'major_damage')
    incident_severity_minor_damage = int(myform.getlist('incident_severity')[0] == 'minor_damage')
    incident_severity_total_loss = int(myform.getlist('incident_severity')[0] == 'total_loss')
    incident_severity_trivial_damage = int(myform.getlist('incident_severity')[0] == 'trivial_damage')

    husband = int(myform.getlist('insured_relationship')[0] == 'husband')
    not_in_family =int(myform.getlist('insured_relationship')[0] == 'not_in_family')
    otherrelative = int(myform.getlist('insured_relationship')[0] == 'other_relative')
    child = int(myform.getlist('insured_relationship')[0] == 'child' )
    unmarried = int(myform.getlist('insured_relationship')[0] == 'unmarried')
    wife = int(myform.getlist('insured_relationship')[0] == 'wife')

    collision_type_unknown = int(myform.getlist('collision_type')[0] == 'collision_type_unknown')
    collision_type_front_collision = int(myform.getlist('collision_type')[0] == 'collision_type_front')
    collision_type_rear_collision = int(myform.getlist('collision_type')[0] == 'collision_type_rear')
    collision_type_side_collision = int(myform.getlist('collision_type')[0] == 'collision_type_side')

    policyIL = int(myform.getlist('policy_state')[0] == 'policy_IL')
    policyIN = int(myform.getlist('policy_state')[0] == 'policy_IN')
    policyOH = int(myform.getlist('policy_state')[0] == 'policy_OH')

    csl100 = int(myform.getlist('policy_csl')[0] == 'csl100')
    csl250 = int(myform.getlist('policy_csl')[0] == 'csl250')
    csl500 = int(myform.getlist('policy_csl')[0] == 'csl500')


    inputs = [[months, age, policy_deduct, policy_annual, umbrella_limit, capital_gains, capital_loss,
            number_vehicle, body, witnesses, total_claim_amount, policyIL, policyIN, policyOH, csl100,
            csl250, csl500, int(insured_sex =='F'), int(insured_sex =='M'), associate, college, highschool,
            jd, md, masters, phd, insured_occupation_adm_clerical, insured_occupation_armed_forces, insured_occupation_craft_repair,
            insured_occupation_exec_managerial, insured_occupation_farming_fishing, insured_occupation_handlers_cleaners,
            insured_occupation_machine_op_inspct, insured_occupation_other_service, insured_occupation_priv_house_service,
            insured_occupation_prof_specialty, insured_occupation_protective_serv, insured_occupation_sales,
            insured_occupation_tech_support, insured_occupation_transport_moving, basejumping, basketball,
            boardgames,bungiejumping, camping, chess, crossfit, dancing, exercise, golf, hiking, kayaking,
            movies, paintball, polo, reading, skydiving, sleeping, videogames, yachting, husband, not_in_family, otherrelative, child,
            unmarried, wife, incident_type_multivehicle_collision, incident_type_parked_car, incident_type_single_vehicle, incident_type_vehicle_theft,
            collision_type_front_collision, collision_type_rear_collision, collision_type_side_collision,
            collision_type_unknown, incident_severity_major_damage, incident_severity_minor_damage, 
            incident_severity_total_loss, incident_severity_trivial_damage, stateNC, stateNY, stateOH, 
            statePA, stateSC, stateVA, stateWV, arlington, columbus, hillsdale, northbend, northbrook,
            riverwood, springfield, int(property_damage == 'damage_NO'), int(property_damage == 'damage_YES'), 
            int(police_report =='report_NO'), int(police_report =='report_YES'), accura, audi, bmw, chev,
             dodge, ford, honda, jeep, mercy, nissan, saab, suburu, toyota, volks]]
    
    df = pd.DataFrame(inputs, columns=['months_as_customer', 'age', 'policy_deductable', 'policy_annual_premium',
    'umbrella_limit', 'capital-gains','capital-loss', 'number_of_vehicles_involved', 'bodily_injuries','witnesses',
    'total_claim_amount','policy_state_IL','policy_state_IN','policy_state_OH', 'policy_csl_100','policy_csl_250/500',
    'policy_csl_500/1000','insured_sex_FEMALE','insured_sex_MALE', 'insured_education_level_Associate',
    'insured_education_level_College','insured_education_level_High School', 'insured_education_level_JD',
    'insured_education_level_MD', 'insured_education_level_Masters','insured_education_level_PhD',
    'insured_occupation_adm-clerical','insured_occupation_armed-forces','insured_occupation_craft-repair',
    'insured_occupation_exec-managerial','insured_occupation_farming-fishing','insured_occupation_handlers-cleaners',
    'insured_occupation_machine-op-inspct','insured_occupation_other-service','insured_occupation_priv-house-serv',
    'insured_occupation_prof-specialty','insured_occupation_protective-serv', 'insured_occupation_sales',
    'insured_occupation_tech-support','insured_occupation_transport-moving','insured_hobbies_base-jumping',
    'insured_hobbies_basketball','insured_hobbies_board-games', 'insured_hobbies_bungie-jumping','insured_hobbies_camping','insured_hobbies_chess',
    'insured_hobbies_cross-fit', 'insured_hobbies_dancing','insured_hobbies_exercise', 'insured_hobbies_golf',
    'insured_hobbies_hiking', 'insured_hobbies_kayaking','insured_hobbies_movies','insured_hobbies_paintball',
    'insured_hobbies_polo', 'insured_hobbies_reading','insured_hobbies_skydiving', 'insured_hobbies_sleeping',
    'insured_hobbies_video-games', 'insured_hobbies_yachting','insured_relationship-husband',
    'insured_relationship_not-in-family','insured_relationship_other-relative', 'insured_relationship_own-child',
    'insured_relationship_unmarried', 'insured_relationship_wife','incident_type_Multi-vehicle collision',
    'incident_type_Parked Car', 'incident_type_Single Vehicle Collision','incident_type_Vehicle Theft',
    'collision_type_Front Collision','collision_type_Rear Collision','collision_type_Side Collision', 
    'collision_type_Unknown', 'incident_severity_Major Damage', 'incident_severity_Minor Damage',
    'incident_severity_Total Loss','incident_severity_Trivial Damage', 'incident_state_NC', 'incident_state_NY',
    'incident_state_OH', 'incident_state_PA', 'incident_state_SC','incident_state_VA', 'incident_state_WV',
    'incident_city_Arlington', 'incident_city_Columbus','incident_city_Hillsdale', 'incident_city_Northbend',
    'incident_city_Northbrook', 'incident_city_Riverwood','incident_city_Springfield', 'property_damage_NO',
    'property_damage_YES', 'police_report_available_NO','police_report_available_YES', 'auto_make_Accura',
    'auto_make_Audi', 'auto_make_BMW','auto_make_Chevrolet', 'auto_make_Dodge', 'auto_make_Ford','auto_make_Honda',
    'auto_make_Jeep', 'auto_make_Mercedes','auto_make_Nissan', 'auto_make_Saab', 'auto_make_Suburu',
    'auto_make_Toyota', 'auto_make_Volkswagen'])

    scaled_feature = scaler.transform(df)

    pred=model.predict(scaled_feature)
    proba = model.predict_proba(scaled_feature)

    if pred == 1:
        prbb = round(np.max(proba*100), 2)
        rslt = "FRAUD"
        color = "yellow"
            
    else:
        prbb = round(np.max(proba*100), 2)
        rslt = "NOT FRAUD"
        color = "blue"

    return render_template(
        'go.html',
        result=pred, res = rslt, proba = prbb, color = color
    )

# Error handling
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')


 
if __name__ == '__main__':
    scaler = joblib.load("scale data") # load scaler
    model = joblib.load("model_svc_tuned")
    app.run(host='127.0.0.1', port=3004, debug=True)
