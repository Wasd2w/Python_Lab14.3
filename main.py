import json
import matplotlib.pyplot as plt

def load_json_file(file_name):
    try:
        with open(file_name, 'r') as file:
            data = json.load(file)
            return data
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error loading JSON file '{file_name}': {e}")
        return None

def display_json_content(data):
    if data is not None:
        print("JSON Content:")
        print(json.dumps(data, indent=2))

def add_entry(data, name, height, gender):
    new_entry = {"name": name, "height": height, "gender": gender}
    data.append(new_entry)
    print(f"New entry added: {new_entry}")

def remove_entry(data, name):
    for entry in data:
        if entry["name"] == name:
            data.remove(entry)
            print(f"Entry removed: {entry}")
            return
    print(f"No entry found with name: {name}")

def search_by_field(data, field, value):
    results = [entry for entry in data if entry.get(field) == value]
    if results:
        print(f"Search results for {field}={value}:")
        print(json.dumps(results, indent=2))
    else:
        print(f"No entries found with {field}={value}")

def calculate_average_height(data, gender):
    heights = [entry["height"] for entry in data if entry["gender"] == gender]
    if heights:
        average_height = sum(heights) / len(heights)
        return average_height
    else:
        return None

def main():
    input_file_name = 'height_data.json'
    output_file_name = 'result.json'

    data = load_json_file(input_file_name)

    if data is not None:
        display_json_content(data)

        # ... (previous code remains unchanged)

        # Create a pie chart for the gender distribution
        gender_counts = {"male": 0, "female": 0}

        for entry in data:
            if entry.get("gender") in gender_counts:
                gender_counts[entry["gender"]] += 1

        labels = list(gender_counts.keys())
        sizes = list(gender_counts.values())
        colors = ['blue', 'pink']  # You can customize the colors as needed

        plt.figure(figsize=(8, 8))
        plt.pie(sizes, labels=labels, autopct='%1.1f%%', colors=colors, startangle=90)
        plt.title('Gender Distribution')
        plt.show()

        average_height_male = calculate_average_height(data, "male")
        if average_height_male is not None:
            print(f"Average height of males: {average_height_male:.2f}")

        result_data = {"average_height_male": average_height_male}
        with open(output_file_name, 'w') as result_file:
            json.dump(result_data, result_file, indent=2)
            print(f"Result saved to '{output_file_name}'")

if __name__ == "__main__":
    main()
