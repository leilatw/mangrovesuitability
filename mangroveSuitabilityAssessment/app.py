from flask import Flask, render_template, request
app = Flask(__name__)

# Define parameters, scores, and weights for each mangrove type
PARAMETERS_SONNERATIA_ALBA = {
    "Sediment Supply": ["Very Low", "Low (1-3)", "Moderate (4-6)", "High (7-9)"],
    "Soil Texture": ["Sandy", "Silty Clay", "Sandy-Clay", "Clay"],
    "Rainfall pattern (mm/year)": ["<500", "500-1500", "1500-2500", ">2500"],
    "Temperature (°C)": ["<0", "0-20", "20-30", ">30"],
    "Inundation duration (times/month)": ["<5", "5-10", "10-20", ">20"],
    "Tidal range (cm)": ["<20", "20-40", "40-60", ">60"],
    "Wind and wave loads": ["Light", "Moderate", "High", "Very High"],
    "Water salinity (%)": ["0-5", "5-15", "15-30", ">30"],
    "Presence of pollutant": ["None", "Low (trace levels)", "Moderate (tolerable)", "High (harmful levels)"],
    "Nutrient content": ["Poor (depleted)", "Fair", "Good", "Excellent (rich)"],
    "pH": ["<6", "6-6.5", "6.5-7.3", ">7.3"],
    "Salinity levels (ppt)": ["0-5", "5-15", "15-35", ">35"],
    "Connectivity to species": ["Isolated", "Low connectivity", "Moderate connectivity", "High connectivity"],
    "Local Engagement": ["Low", "Moderate", "High", "Very High"],
    "Sustainable use": ["Unsustainable", "Slightly sustainable", "Sustainable", "Highly sustainable"],
    "Upstream Disturbance": ["Severe (>20 events/yr)", "Moderate (10-20 events/yr)", "Mild (5-10 events/yr)",
                             "Minimal (<5 events/yr)"],
    "Existing Laws": ["Nonexistent", "Weak", "Moderate", "Strong"],
    "Law Enforcement": ["None", "Rarely enforced", "Occasionally enforced", "Strictly enforced"]
}

SCORES_SONNERATIA_ALBA = {
    "Sediment Supply": [10, 20, 30, 40],
    "Soil Texture": [10, 20, 30, 40],
    "Rainfall pattern (mm/year)": [10, 20, 30, 40],
    "Temperature (°C)": [10, 20, 30, 40],
    "Inundation duration (times/month)": [10, 20, 30, 40],
    "Tidal range (cm)": [10, 20, 30, 40],
    "Wind and wave loads": [10, 20, 30, 40],
    "Water salinity (%)": [10, 20, 30, 40],
    "Presence of pollutant": [10, 20, 30, 40],
    "Nutrient content": [10, 20, 30, 40],
    "pH": [10, 20, 30, 40],
    "Salinity levels (ppt)": [10, 20, 30, 40],
    "Connectivity to species": [10, 20, 30, 40],
    "Local Engagement": [10, 20, 30, 40],
    "Sustainable use": [10, 20, 30, 40],
    "Upstream Disturbance": [10, 20, 30, 40],
    "Existing Laws": [10, 20, 30, 40],
    "Law Enforcement": [10, 20, 30, 40]
}

WEIGHTS_SONNERATIA_ALBA = {
    "Sediment Supply": 1.2,
    "Soil Texture": 1.5,
    "Rainfall pattern (mm/year)": 1.2,
    "Temperature (°C)": 1.7,
    "Inundation duration (times/month)": 1.1,
    "Tidal range (cm)": 1.4,
    "Wind and wave loads": 1.8,
    "Water salinity (%)": 1.1,
    "Presence of pollutant": 1.2,
    "Nutrient content": 1.4,
    "pH": 1.7,
    "Salinity levels (ppt)": 1.2,
    "Connectivity to species": 1.2,
    "Local Engagement": 1.6,
    "Sustainable use": 1.5,
    "Upstream Disturbance": 1.8,
    "Existing Laws": 1.4,
    "Law Enforcement": 1.9
}

PARAMETERS_AVICENNIA_MARINA = {
    "Sediment Supply": ["Very Low", "Low (1-3)", "Moderate (4-6)", "High (7-9)"],
    "Soil Texture": ["Sandy", "Silty Clay", "Sandy-Clay", "Clay"],
    "Rainfall pattern (mm/year)": ["<500", "500-1500", "1500-2500", ">2500"],
    "Temperature (°C)": ["<0", "0-20", "20-30", ">30"],
    "Inundation duration (times/month)": ["<5", "5-10", "10-20", ">20"],
    "Tidal range (cm)": ["<20", "20-40", "40-60", ">60"],
    "Wind and wave loads": ["Light", "Moderate", "High", "Very High"],
    "Water salinity (%)": ["0-5", "5-15", "15-30", ">30"],
    "Presence of pollutant": ["None", "Low (trace levels)", "Moderate (tolerable)", "High (harmful levels)"],
    "Nutrient content": ["Poor (depleted)", "Fair", "Good", "Excellent (rich)"],
    "pH": ["<6", "6-6.5", "6.5-7.3", ">7.3"],
    "Salinity levels (ppt)": ["0-5", "5-15", "15-35", ">35"],
    "Connectivity to species": ["Isolated", "Low connectivity", "Moderate connectivity", "High connectivity"],
    "Local Engagement": ["Low", "Moderate", "High", "Very High"],
    "Sustainable use": ["Unsustainable", "Slightly sustainable", "Sustainable", "Highly sustainable"],
    "Upstream Disturbance": ["Severe (>20 events/yr)", "Moderate (10-20 events/yr)", "Mild (5-10 events/yr)",
                             "Minimal (<5 events/yr)"],
    "Existing Laws": ["Nonexistent", "Weak", "Moderate", "Strong"],
    "Law Enforcement": ["None", "Rarely enforced", "Occasionally enforced", "Strictly enforced"]
}

SCORES_AVICENNIA_MARINA = {
    "Sediment Supply": [10, 20, 30, 40],
    "Soil Texture": [10, 20, 30, 40],
    "Rainfall pattern (mm/year)": [10, 20, 30, 40],
    "Temperature (°C)": [10, 20, 30, 40],
    "Inundation duration (times/month)": [10, 20, 30, 40],
    "Tidal range (cm)": [10, 20, 30, 40],
    "Wind and wave loads": [10, 20, 30, 40],
    "Water salinity (%)": [10, 20, 30, 40],
    "Presence of pollutant": [10, 20, 30, 40],
    "Nutrient content": [10, 20, 30, 40],
    "pH": [10, 20, 30, 40],
    "Salinity levels (ppt)": [10, 20, 30, 40],
    "Connectivity to species": [10, 20, 30, 40],
    "Local Engagement": [10, 20, 30, 40],
    "Sustainable use": [10, 20, 30, 40],
    "Upstream Disturbance": [10, 20, 30, 40],
    "Existing Laws": [10, 20, 30, 40],
    "Law Enforcement": [10, 20, 30, 40]
}

WEIGHTS_AVICENNIA_MARINA = {
    "Sediment Supply": 1.2,
    "Soil Texture": 1.5,
    "Rainfall pattern (mm/year)": 1.2,
    "Temperature (°C)": 1.7,
    "Inundation duration (times/month)": 1.1,
    "Tidal range (cm)": 1.4,
    "Wind and wave loads": 1.8,
    "Water salinity (%)": 1.1,
    "Presence of pollutant": 1.2,
    "Nutrient content": 1.4,
    "pH": 1.7,
    "Salinity levels (ppt)": 1.2,
    "Connectivity to species": 1.2,
    "Local Engagement": 1.6,
    "Sustainable use": 1.5,
    "Upstream Disturbance": 1.8,
    "Existing Laws": 1.4,
    "Law Enforcement": 1.9
}

PARAMETERS_RHIZOPHORA_MANGLE = {
    "Sediment Supply": ["Very Low", "Low (1-3)", "Moderate (4-6)", "High (7-9)"],
    "Soil Texture": ["Sandy", "Silty Clay", "Sandy-Clay", "Clay"],
    "Rainfall pattern (mm/year)": ["<500", "500-1500", "1500-2500", ">2500"],
    "Temperature (°C)": ["<0", "0-20", "20-30", ">30"],
    "Inundation duration (times/month)": ["<5", "5-10", "10-20", ">20"],
    "Tidal range (cm)": ["<20", "20-40", "40-60", ">60"],
    "Wind and wave loads": ["Light", "Moderate", "High", "Very High"],
    "Water salinity (%)": ["0-5", "5-15", "15-30", ">30"],
    "Presence of pollutant": ["None", "Low (trace levels)", "Moderate (tolerable)", "High (harmful levels)"],
    "Nutrient content": ["Poor (depleted)", "Fair", "Good", "Excellent (rich)"],
    "pH": ["<6", "6-6.5", "6.5-7.3", ">7.3"],
    "Salinity levels (ppt)": ["0-5", "5-15", "15-35", ">35"],
    "Connectivity to species": ["Isolated", "Low connectivity", "Moderate connectivity", "High connectivity"],
    "Local Engagement": ["Low", "Moderate", "High", "Very High"],
    "Sustainable use": ["Unsustainable", "Slightly sustainable", "Sustainable", "Highly sustainable"],
    "Upstream Disturbance": ["Severe (>20 events/yr)", "Moderate (10-20 events/yr)", "Mild (5-10 events/yr)",
                             "Minimal (<5 events/yr)"],
    "Existing Laws": ["Nonexistent", "Weak", "Moderate", "Strong"],
    "Law Enforcement": ["None", "Rarely enforced", "Occasionally enforced", "Strictly enforced"]
}

SCORES_RHIZOPHORA_MANGLE = {
    "Sediment Supply": [10, 20, 30, 40],
    "Soil Texture": [10, 20, 30, 40],
    "Rainfall pattern (mm/year)": [10, 20, 30, 40],
    "Temperature (°C)": [10, 20, 30, 40],
    "Inundation duration (times/month)": [10, 20, 30, 40],
    "Tidal range (cm)": [10, 20, 30, 40],
    "Wind and wave loads": [10, 20, 30, 40],
    "Water salinity (%)": [10, 20, 30, 40],
    "Presence of pollutant": [10, 20, 30, 40],
    "Nutrient content": [10, 20, 30, 40],
    "pH": [10, 20, 30, 40],
    "Salinity levels (ppt)": [10, 20, 30, 40],
    "Connectivity to species": [10, 20, 30, 40],
    "Local Engagement": [10, 20, 30, 40],
    "Sustainable use": [10, 20, 30, 40],
    "Upstream Disturbance": [10, 20, 30, 40],
    "Existing Laws": [10, 20, 30, 40],
    "Law Enforcement": [10, 20, 30, 40]
}

WEIGHTS_RHIZOPHORA_MANGLE = {
    "Sediment Supply": 1.2,
    "Soil Texture": 1.5,
    "Rainfall pattern (mm/year)": 1.2,
    "Temperature (°C)": 1.7,
    "Inundation duration (times/month)": 1.1,
    "Tidal range (cm)": 1.4,
    "Wind and wave loads": 1.8,
    "Water salinity (%)": 1.1,
    "Presence of pollutant": 1.2,
    "Nutrient content": 1.4,
    "pH": 1.7,
    "Salinity levels (ppt)": 1.2,
    "Connectivity to species": 1.2,
    "Local Engagement": 1.6,
    "Sustainable use": 1.5,
    "Upstream Disturbance": 1.8,
    "Existing Laws": 1.4,
    "Law Enforcement": 1.9
}

PARAMETERS_CERIOPS_TAGAL = {
    "Sediment Supply": ["Very Low", "Low (1-3)", "Moderate (4-6)", "High (7-9)"],
    "Soil Texture": ["Sandy", "Silty Clay", "Sandy-Clay", "Clay"],
    "Rainfall pattern (mm/year)": ["<500", "500-1500", "1500-2500", ">2500"],
    "Temperature (°C)": ["<0", "0-20", "20-30", ">30"],
    "Inundation duration (times/month)": ["<5", "5-10", "10-20", ">20"],
    "Tidal range (cm)": ["<20", "20-40", "40-60", ">60"],
    "Wind and wave loads": ["Light", "Moderate", "High", "Very High"],
    "Water salinity (%)": ["0-5", "5-15", "15-30", ">30"],
    "Presence of pollutant": ["None", "Low (trace levels)", "Moderate (tolerable)", "High (harmful levels)"],
    "Nutrient content": ["Poor (depleted)", "Fair", "Good", "Excellent (rich)"],
    "pH": ["<6", "6-6.5", "6.5-7.3", ">7.3"],
    "Salinity levels (ppt)": ["0-5", "5-15", "15-35", ">35"],
    "Connectivity to species": ["Isolated", "Low connectivity", "Moderate connectivity", "High connectivity"],
    "Local Engagement": ["Low", "Moderate", "High", "Very High"],
    "Sustainable use": ["Unsustainable", "Slightly sustainable", "Sustainable", "Highly sustainable"],
    "Upstream Disturbance": ["Severe (>20 events/yr)", "Moderate (10-20 events/yr)", "Mild (5-10 events/yr)",
                             "Minimal (<5 events/yr)"],
    "Existing Laws": ["Nonexistent", "Weak", "Moderate", "Strong"],
    "Law Enforcement": ["None", "Rarely enforced", "Occasionally enforced", "Strictly enforced"]
}

SCORES_CERIOPS_TAGAL = {
    "Sediment Supply": [10, 20, 30, 40],
    "Soil Texture": [10, 20, 30, 40],
    "Rainfall pattern (mm/year)": [10, 20, 30, 40],
    "Temperature (°C)": [10, 20, 30, 40],
    "Inundation duration (times/month)": [10, 20, 30, 40],
    "Tidal range (cm)": [10, 20, 30, 40],
    "Wind and wave loads": [10, 20, 30, 40],
    "Water salinity (%)": [10, 20, 30, 40],
    "Presence of pollutant": [10, 20, 30, 40],
    "Nutrient content": [10, 20, 30, 40],
    "pH": [10, 20, 30, 40],
    "Salinity levels (ppt)": [10, 20, 30, 40],
    "Connectivity to species": [10, 20, 30, 40],
    "Local Engagement": [10, 20, 30, 40],
    "Sustainable use": [10, 20, 30, 40],
    "Upstream Disturbance": [10, 20, 30, 40],
    "Existing Laws": [10, 20, 30, 40],
    "Law Enforcement": [10, 20, 30, 40]
}

WEIGHTS_CERIOPS_TAGAL = {
    "Sediment Supply": 1.2,
    "Soil Texture": 1.5,
    "Rainfall pattern (mm/year)": 1.2,
    "Temperature (°C)": 1.7,
    "Inundation duration (times/month)": 1.1,
    "Tidal range (cm)": 1.4,
    "Wind and wave loads": 1.8,
    "Water salinity (%)": 1.1,
    "Presence of pollutant": 1.2,
    "Nutrient content": 1.4,
    "pH": 1.7,
    "Salinity levels (ppt)": 1.2,
    "Connectivity to species": 1.2,
    "Local Engagement": 1.6,
    "Sustainable use": 1.5,
    "Upstream Disturbance": 1.8,
    "Existing Laws": 1.4,
    "Law Enforcement": 1.9
}

# Function to calculate the score
def calculate_score(user_scores, weights):
    total_weight = sum(weights.values())
    weighted_score = sum(user_scores[param] * weights[param] for param in user_scores)
    max_score = sum(max(SCORES_CERIOPS_TAGAL[param]) * weights[param] for param in weights)
    return (weighted_score / max_score) * 100 if max_score else 0


# Route for selecting the mangrove type
@app.route('/', methods=['GET'])
def select_mangrove():
    return render_template('select_mangrove.html')

@app.route('/assessment', methods=['POST'])
def assessment():
    mangrove_type = request.form.get('mangrove_type')

    # Select the correct set of parameters based on the mangrove type
    if mangrove_type == 'sonneratia_alba':
        parameters = PARAMETERS_SONNERATIA_ALBA
    elif mangrove_type == 'avicennia_marina':
        parameters = PARAMETERS_AVICENNIA_MARINA
    elif mangrove_type == 'rhizophora_mangle':
        parameters = PARAMETERS_RHIZOPHORA_MANGLE
    else:  # Default to CERIOPS_TAGAL if no match or another type is added
        parameters = PARAMETERS_CERIOPS_TAGAL

    return render_template('assessment.html', parameters=parameters, mangrove_type=mangrove_type)


@app.route('/results', methods=['POST'])
def results():
    mangrove_type = request.form.get('mangrove_type')
    print("Mangrove Type Selected:", mangrove_type)

    # Set the correct scores and weights based on the mangrove type
    if mangrove_type == 'sonneratia_alba':
        parameters = PARAMETERS_SONNERATIA_ALBA
        scores_dict = SCORES_SONNERATIA_ALBA
        weights = WEIGHTS_SONNERATIA_ALBA
    elif mangrove_type == 'avicennia_marina':
        parameters = PARAMETERS_AVICENNIA_MARINA
        scores_dict = SCORES_AVICENNIA_MARINA
        weights = WEIGHTS_AVICENNIA_MARINA
    elif mangrove_type == 'rhizophora_mangle':
        parameters = PARAMETERS_RHIZOPHORA_MANGLE
        scores_dict = SCORES_RHIZOPHORA_MANGLE
        weights = WEIGHTS_RHIZOPHORA_MANGLE
    else:
        parameters = PARAMETERS_CERIOPS_TAGAL
        scores_dict = SCORES_CERIOPS_TAGAL
        weights = WEIGHTS_CERIOPS_TAGAL

    user_scores = {}
    percentage_losses = {}  # To track percentage losses for each parameter
    total_max_possible_score = 0
    total_user_score = 0

    for parameter in parameters:
        max_param_score = max(scores_dict[parameter])
        total_max_possible_score += max_param_score * weights[parameter]

        choice = request.form.get(parameter)
        if choice:
            index = parameters[parameter].index(choice)
            user_scores[parameter] = scores_dict[parameter][index]
            total_user_score += user_scores[parameter] * weights[parameter]

    for parameter in parameters:
        max_param_score = max(scores_dict[parameter])
        user_score = user_scores.get(parameter, 0)
        loss = (max_param_score - user_score) * weights[parameter]
        percentage_loss = (loss / total_max_possible_score) * 100
        percentage_losses[parameter] = round(percentage_loss, 1)

    final_score = (total_user_score / total_max_possible_score) * 100 if total_max_possible_score else 0

    # Sort parameters by highest percentage loss and select top 3
    top_improvements = sorted(percentage_losses.items(), key=lambda x: x[1], reverse=True)[:5]

    return render_template('results.html', final_score=final_score, mangrove_type=mangrove_type,
                           improvements=top_improvements)

if __name__ == '__main__':
    app.run(debug=True)
