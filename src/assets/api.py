from flask import Flask, jsonify

app = Flask(__name__)

# Sample data
data = {
  "TimeLine": {
    "ClassicalEra": [
      {
        "AncientGreece": {
          "Works": {
            "The Charioteer of Delphi": {
              "id": 1,
              "Author": "Unknown",
              "Date": "5th century BC",
              "Description": "The Charioteer of Delphi is a Greek sculpture that represents a charioteer in a chariot. The sculpture is located in the Delphi Archaeological Museum.",
              "Image": "https://upload.wikimedia.org/wikipedia/commons/1/1d/Kouros_An%C3%B3nimo_01.jpg",
              "Museum": "Delphi Archaeological Museum"
            },
            "Pottery of Musical Scenes": {
              "id": 2,
              "Author": "Unknown",
              "Date": "6th century BC",
              "Description": "The Pottery of Musical Scenes is a Greek ceramic that depicts musicians and dancers. The ceramic is located in the Walters Art Museum in Baltimore.",
              "Image": "https://upload.wikimedia.org/wikipedia/commons/1/1d/Kouros_An%C3%B3nimo_01.jpg",
              "Museum": "Walters Art Museum in Baltimore"
            },
            "Discobolus of Myron": {
              "id": 3,
              "Author": "Unknown",
              "Date": "5th century BC",
              "Description": "The Discobolus of Myron is a Greek sculpture that represents an athlete throwing a discus. The sculpture is located in the National Roman Museum in Rome.",
              "Image": "https://upload.wikimedia.org/wikipedia/commons/1/1d/Kouros_An%C3%B3nimo_01.jpg",
              "Museum": "National Roman Museum in Rome"
            },
            "Bronze Nike": {
              "id": 4,
              "Author": "Unknown",
              "Date": "5th century BC",
              "Description": "The Bronze Nike is a Greek sculpture that represents the goddess Nike. The sculpture is located in the Louvre Museum in Paris.",
              "Image": "https://upload.wikimedia.org/wikipedia/commons/1/1d/Kouros_An%C3%B3nimo_01.jpg",
              "Museum": "Louvre Museum in Paris"
            },
            "Doryphoros by Polykleitos": {
              "id": 5,
              "Author": "Unknown",
              "Date": "5th century BC",
              "Description": "The Doryphoros by Polykleitos is a Greek sculpture that represents a man with a lyre. The sculpture is located in the National Archaeological Museum in Naples.",
              "Image": "https://upload.wikimedia.org/wikipedia/commons/1/1d/Kouros_An%C3%B3nimo_01.jpg",
              "Museum": "National Archaeological Museum, Naples"
            },
            "Parthenon": {
              "id": 6,
              "Author": "Ictinus, Callicrates, and Phidias",
              "Date": "5th century BC",
              "Description": "The Parthenon is a Doric temple dedicated to the goddess Athena, built on the Acropolis of Athens. It is one of the masterpieces of classical Greek architecture.",
              "Image": "https://upload.wikimedia.org/wikipedia/commons/1/1d/Kouros_An%C3%B3nimo_01.jpg",
              "Museum": "Acropolis of Athens"
            }
          }
        },
        "AncientRome": [
        ]
      }
    ],
    "MedievalEra": [
      {
        "EarlyMedieval": [],
        "Romanesque": [],
        "Gothic": []
      }
    ],
    "LongNeoclassicism": [
      {
        "Renaissance": [],
        "Baroque": [],
        "Neoclassicism": []
      }
    ],
    "19thCentury": [
      {
        "Romanticism": [],
        "Realism": [],
        "Impressionism": []
      }
    ],
    "20thCentury": [
      {
        "ModernArt": [],
        "PostmodernArt": []
      }
    ],
    "ContemporaryEra": [
      {
        "ContemporaryArt": []
      }
    ]
  }
}

@app.route('/api/items', methods=['GET'])
def get_items():
    return jsonify(data)

@app.route('/api/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    # Searching for an item by ID across all works in Ancient Greece
    works = data['TimeLine']['ClassicalEra'][0]['AncientGreece']['Works']
    for work in works.values():
        if work['id'] == item_id:
            return jsonify(work)
    return '', 404

if __name__ == '__main__':
    app.run(debug=True)  # Run the application