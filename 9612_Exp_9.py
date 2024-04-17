#Gaurav_Joshi_9612_BatchD
class ExpertSystem:
    def __init__(self):
        self.rules = {
            "low_calorie": "Focus on consuming fruits, vegetables, lean proteins, and whole grains. Limit added sugars and fats.",
            "high_protein": "Include plenty of protein-rich foods such as lean meats, fish, eggs, dairy, legumes, and nuts.",
            "low_carb": "Limit carbohydrate intake and focus on consuming non-starchy vegetables, lean proteins, and healthy fats.",
            "balanced_diet": "Eat a variety of foods from all food groups, including fruits, vegetables, grains, protein-rich foods, and healthy fats.",
            "low_fat": "Choose foods that are naturally low in fat such as fruits, vegetables, and lean proteins.",
            "gluten_free": "Avoid foods containing gluten such as wheat, barley, and rye. Focus on naturally gluten-free foods like fruits, vegetables, lean meats, and gluten-free grains.",
            "dairy_free": "Avoid dairy products and choose dairy-free alternatives such as soy milk, almond milk, and coconut yogurt.",
            "vegetarian": "Avoid meat and fish. Include plant-based sources of protein such as beans, lentils, tofu, and tempeh.",
            "vegan": "Avoid all animal products including meat, fish, dairy, and eggs. Focus on plant-based foods.",
            "low_sodium": "Limit salt intake and choose foods that are low in sodium. Avoid processed foods and choose fresh or homemade options.",
            # Add more rules here as needed
        }

    def consult(self, dietary_needs):
        recommendations = []
        for need in dietary_needs:
            if need in self.rules:
                recommendations.append(self.rules[need])
            else:
                recommendations.append("Sorry, I'm not sure what to advise for '{}' dietary need.".format(need))
        return recommendations

def main():
    expert_system = ExpertSystem()

    # Example consultations
    print("Dietary needs: low_calorie, high_protein")
    print(expert_system.consult(["low_calorie", "high_protein"]))

    print("\nDietary needs: low_carb, balanced_diet")
    print(expert_system.consult(["low_carb", "balanced_diet"]))

    print("\nDietary needs: low_fat, gluten_free, vegetarian")
    print(expert_system.consult(["low_fat", "gluten_free", "vegetarian"]))

    print("\nDietary needs: vegan, low_sodium")
    print(expert_system.consult(["vegan", "low_sodium"]))

if __name__ == "__main__":
    main()

# C:\Users\SCI\OneDrive\Desktop\Gaurav Joshi Codes\AI EXPS>python 9612_Exp_9.py
# Dietary needs: low_calorie, high_protein
# ['Focus on consuming fruits, vegetables, lean proteins, and whole grains. Limit added sugars and fats.', 'Include plenty of protein-rich foods such as lean meats, fish, eggs, dairy, legumes, and nuts.']

# Dietary needs: low_carb, balanced_diet
# ['Limit carbohydrate intake and focus on consuming non-starchy vegetables, lean proteins, and healthy fats.', 'Eat a variety of foods from all food groups, including fruits, vegetables, grains, protein-rich foods, and healthy fats.']

# Dietary needs: low_fat, gluten_free, vegetarian
# ['Choose foods that are naturally low in fat such as fruits, vegetables, and lean proteins.', 'Avoid foods containing gluten such as wheat, barley, and rye. Focus on naturally gluten-free foods like fruits, vegetables, lean meats, and gluten-free grains.', 'Avoid meat and fish. Include plant-based sources of protein such as beans, lentils, tofu, and tempeh.']

# Dietary needs: vegan, low_sodium
# ['Avoid all animal products including meat, fish, dairy, and eggs. Focus on plant-based foods.', 'Limit salt intake and choose foods that are low in sodium. Avoid processed foods and choose fresh or homemade options.']
