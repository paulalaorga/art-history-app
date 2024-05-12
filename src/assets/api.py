from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Sample data
{
  "TimeLine": {
    "ClassicalEra": [
      {
        "Years": "500 - 323 BC",
        "Periods": {
          "AncientGreece": {
            "Years": "500 - 323 BC",
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
                "Museum": "National Archaeological Museum in Naples"
              },
              "Parthenon": {
                "id": 6,
                "Author": "Ictinus, Callicrates, and Phidias",
                "Date": "5th century BC",
                "Description": "The Parthenon is a Doric temple dedicated to the goddess Athena, built on the Acropolis of Athens. It is one of the masterpieces of classical Greek architecture.",
                "Image": "https://upload.wikimedia.org/wikipedia/commons/1/1d/Kouros_An%C3%B3nimo_01.jpg",
                "Museum": "Acropolis of Athens"
              },
              "Bronze of Riace": {
                "id": 7,
                "Author": "Unknown",
                "Date": "460-450 BC",
                "Description": "The Bronze of Riace are two full-size Greek bronzes of naked bearded warriors, cast about 460–450 BC that were found in the sea near Riace in 1972.",
                "Image": "https://upload.wikimedia.org/wikipedia/commons/1/1d/Kouros_An%C3%B3nimo_01.jpg",
                "Museum": "National Museum of Magna Graecia in Reggio Calabria"
              },
                           "Bust of Plato": {
                "id": 8,
                "Author": "Unknown",
                "Date": "4th century BC",
                "Description": "A bust depicting the ancient Greek philosopher Plato, often considered a foundational figure in Western philosophy.",
                "Image": "https://upload.wikimedia.org/wikipedia/commons/1/1d/Kouros_An%C3%B3nimo_01.jpg",
                "Museum": "Acropolis Museum, Athens"
              },
              "The Kidnap of Persephone": {
                "id": 9,
                "Author": "Unknown",
                "Date": "4th century BC",
                "Description": "A sculpture depicting the mythological event of Hades abducting Persephone to be his queen in the underworld.",
                "Image": "https://upload.wikimedia.org/wikipedia/commons/1/1d/Kouros_An%C3%B3nimo_01.jpg",
                "Museum": "National Archaeological Museum, Athens"
              },
              "Bust of Aristotle": {
                "id": 10,
                "Author": "Unknown",
                "Date": "4th century BC",
                "Description": "A sculptural portrait of Aristotle, one of the greatest philosophers in history, known for his influence on logical and scientific thought.",
                "Image": "https://upload.wikimedia.org/wikipedia/commons/1/1d/Kouros_An%C3%B3nimo_01.jpg",
                "Museum": "Ludovisi Collection, Rome"
              },
              "Helios Chariot": {
                "id": 11,
                "Author": "Unknown",
                "Date": "3rd century BC",
                "Description": "A representation of the sun god Helios driving his chariot across the sky, symbolizing the passage of the sun.",
                "Image": "https://upload.wikimedia.org/wikipedia/commons/1/1d/Kouros_An%C3%B3nimo_01.jpg",
                "Museum": "Rhodes Archaeological Museum"
              },
              "Marriage of Alexander and Barsine": {
                "id": 12,
                "Author": "Unknown",
                "Date": "4th century BC",
                "Description": "A fresco depicting the marriage of Alexander the Great to Barsine, symbolizing the union of Greek and Persian cultures.",
                "Image": "https://upload.wikimedia.org/wikipedia/commons/1/1d/Kouros_An%C3%B3nimo_01.jpg",
                "Museum": "Macedonian Museum of Contemporary Art"
              },
              "Pugilist at Rest": {
                "id": 13,
                "Author": "Unknown",
                "Date": "1st century BC",
                "Description": "A Hellenistic bronze sculpture representing a seated boxer at rest, still wrapped in his fight straps.",
                "Image": "https://upload.wikimedia.org/wikipedia/commons/1/1d/Kouros_An%C3%B3nimo_01.jpg",
                "Museum": "National Roman Museum, Rome"
              },
              "Statue of Lucius Junius Brutus": {
                "id": 14,
                "Author": "Unknown",
                "Date": "Late 6th century BC",
                "Description": "A Roman bronze statue of Lucius Junius Brutus, the founder of the Roman Republic and traditionally one of its first consuls in 509 BC.",
                "Image": "https://upload.wikimedia.org/wikipedia/commons/1/1d/Kouros_An%C3%B3nimo_01.jpg",
                "Museum": "Capitoline Museums, Rome"
              },
              "Winged Victory of Samothrace": {
                "id": 15,
                "Author": "Unknown",
                "Date": "2nd century BC",
                "Description": "A marble sculpture of Nike, the Greek goddess of victory, depicted with wings, originally marking a naval victory.",
                "Image": "https://upload.wikimedia.org/wikipedia/commons/1/1d/Kouros_An%C3%B3nimo_01.jpg",
                "Museum": "Louvre Museum, Paris"
              },
              "Frescos of the Villa of the Mysteries": {
                "id": 16,
                "Author": "Unknown",
                "Date": "1st century BC",
                "Description": "A series of vibrant frescoes found in Pompeii that depict a series of initiation rituals into a mystery cult.",
                "Image": "https://upload.wikimedia.org/wikipedia/commons/1/1d/Kouros_An%C3%B3nimo_01.jpg",
                "Museum": "Villa of the Mysteries, Pompeii, Naples"
              },
                            "Venus de Milo": {
                "id": 17,
                "Author": "Unknown",
                "Date": "130-100 BC",
                "Description": "An ancient Greek statue and one of the most famous works of ancient Greek sculpture, representing Aphrodite, the Greek goddess of love and beauty.",
                "Image": "https://upload.wikimedia.org/wikipedia/commons/1/1d/Kouros_An%C3%B3nimo_01.jpg",
                "Museum": "Louvre Museum, Paris"
              },
              "Aphrodite Menophantos": {
                "id": 18,
                "Author": "Menophantos",
                "Date": "1st century BC",
                "Description": "A Roman copy of a Greek statue by sculptor Menophantos, depicting the goddess Aphrodite.",
                "Image": "https://upload.wikimedia.org/wikipedia/commons/1/1d/Kouros_An%C3%B3nimo_01.jpg",
                "Museum": "Capitoline Museums, Rome"
              },
              "Bust of Tusculum (Portrait of Julius Caesar)": {
                "id": 19,
                "Author": "Unknown",
                "Date": "1st century BC",
                "Description": "One of the most iconic portraits of Julius Caesar, providing a realistic depiction of the Roman dictator.",
                "Image": "https://upload.wikimedia.org/wikipedia/commons/1/1d/Kouros_An%C3%B3nimo_01.jpg",
                "Museum": "Vatican Museums, Rome"
              },
              "Bust of Julius Caesar": {
                "id": 20,
                "Author": "Unknown",
                "Date": "1st century BC",
                "Description": "A marble bust representing Julius Caesar, capturing the authoritative and resolute character of Caesar.",
                "Image": "https://upload.wikimedia.org/wikipedia/commons/1/1d/Kouros_An%C3%B3nimo_01.jpg",
                "Museum": "British Museum, London"
              },
              "Maison Carrée": {
                "id": 21,
                "Author": "Unknown",
                "Date": "1st century AD",
                "Description": "One of the best preserved Roman temple façades, Maison Carrée is an exemplar of Vitruvian architecture.",
                "Image": "https://upload.wikimedia.org/wikipedia/commons/1/1d/Kouros_An%C3%B3nimo_01.jpg",
                "Museum": "Nîmes, France"
              },
              "Bust of Socrates": {
                "id": 22,
                "Author": "Unknown",
                "Date": "4th century BC",
                "Description": "A sculptural bust of Socrates, one of the founders of Western philosophy, known for his contributions to ethics and epistemology.",
                "Image": "https://upload.wikimedia.org/wikipedia/commons/1/1d/Kouros_An%C3%B3nimo_01.jpg",
                "Museum": "Louvre Museum, Paris"
              },
              "Portrait of Paquius Proculus": {
                "id": 23,
                "Author": "Unknown",
                "Date": "1st century AD",
                "Description": "A fresco depicting Paquius Proculus, who was a prominent citizen of Pompeii, shown with his wife.",
                "Image": "https://upload.wikimedia.org/wikipedia/commons/1/1d/Kouros_An%C3%B3nimo_01.jpg",
                "Museum": "National Archaeological Museum, Naples"
              },
              "The Judgment of Paris, Fresco from Pompeii": {
                "id": 24,
                "Author": "Unknown",
                "Date": "1st century AD",
                "Description": "A fresco that vividly depicts the mythological story of Paris awarding the golden apple to Aphrodite, leading to the Trojan War.",
                "Image": "https://upload.wikimedia.org/wikipedia/commons/1/1d/Kouros_An%C3%B3nimo_01.jpg",
                "Museum": "National Archaeological Museum, Naples"
              }
            }
          }
        }
      ]
    }
  }
}
        
        },
        "AncientRome": [
          {
      "Young Hercules": {
        "id": 25,
        "Author": "Unknown",
        "Date": "2nd century AD",
        "Description": "A sculpture depicting a youthful Hercules, highlighting his strength and potential in his early years.",
        "Image": "https://upload.wikimedia.org/wikipedia/commons/1/1d/Kouros_An%C3%B3nimo_01.jpg",
        "Museum": "Capitoline Museums, Rome"
      },
      "Young Woman with Stylus and Tablet (Sappho), Fresco from Pompeii": {
        "id": 26,
        "Author": "Unknown",
        "Date": "1st century AD",
        "Description": "A fresco from Pompeii depicting a young woman, possibly the poet Sappho, with a stylus and wax tablet, symbolizing literary activity.",
        "Image": "https://upload.wikimedia.org/wikipedia/commons/1/1d/Kouros_An%C3%B3nimo_01.jpg",
        "Museum": "National Archaeological Museum, Naples"
      },
      "The Punishment of Dirce, Fresco from Pompeii": {
        "id": 27,
        "Author": "Unknown",
        "Date": "1st century AD",
        "Description": "This dramatic fresco depicts the mythological punishment of Dirce, tied to a wild bull by the sons of Antiope as retribution for her cruelty.",
        "Image": "https://upload.wikimedia.org/wikipedia/commons/1/1d/Kouros_An%C3%B3nimo_01.jpg",
        "Museum": "National Archaeological Museum, Naples"
      },
      "Hercules and Omphale, Fresco from Pompeii": {
        "id": 28,
        "Author": "Unknown",
        "Date": "1st century AD",
        "Description": "A fresco showing Hercules in the service of Omphale, the Lydian queen, where he is often depicted wearing women's clothing and spinning wool.",
        "Image": "https://upload.wikimedia.org/wikipedia/commons/1/1d/Kouros_An%C3%B3nimo_01.jpg",
        "Museum": "National Archaeological Museum, Naples"
      },
      "Helen of Sparta on Her Way to Troy, Fresco from Pompeii": {
        "id": 29,
        "Author": "Unknown",
        "Date": "1st century AD",
        "Description": "A fresco capturing the moment Helen of Sparta is taken to Troy, an event that sparked the Trojan War.",
        "Image": "https://upload.wikimedia.org/wikipedia/commons/1/1d/Kouros_An%C3%B3nimo_01.jpg",
        "Museum": "National Archaeological Museum, Naples"
      },
      "Fayum Portraits": {
        "id": 30,
        "Author": "Various",
        "Date": "1st to 3rd century AD",
        "Description": "A collection of mummy portraits from the Fayum area in Egypt, remarkable for their realism and vivid depiction of ancient faces.",
        "Image": "https://upload.wikimedia.org/wikipedia/commons/1/1d/Kouros_An%C3%B3nimo_01.jpg",
        "Museum": "Various museums"
      },
      "Dionysus (seated on a throne) with Helios, Aphrodite and Other Gods, Fresco from Pompeii": {
        "id": 31,
        "Author": "Unknown",
        "Date": "1st century AD",
        "Description": "A detailed fresco depicting Dionysus alongside other deities such as Helios and Aphrodite, illustrating a scene of divine congregation.",
        "Image": "https://upload.wikimedia.org/wikipedia/commons/1/1d/Kouros_An%C3%B3nimo_01.jpg",
        "Museum": "National Archaeological Museum, Naples"
      },
      "Laocoon and His Sons": {
        "id": 32,
        "Author": "Agesander, Athenodoros, and Polydorus",
        "Date": "Early 1st century AD",
        "Description": "This famous sculpture shows the Trojan priest Laocoon and his sons being attacked by sea serpents, highlighting the suffering and struggle.",
        "Image": "https://upload.wikimedia.org/wikipedia/commons/a/af/Laocoon_group_Vatican.JPG",
        "Museum": "Vatican Museums, Rome"
      },
      "Pont du Gard (France)": {
        "id": 33,
        "Author": "Unknown",
        "Date": "1st century AD",
        "Description": "An ancient Roman aqueduct bridge that crosses the Gardon River in southern France, exemplifying Roman architectural brilliance and utility.",
        "Image": "https://upload.wikimedia.org/wikipedia/commons/1/1d/Kouros_An%C3%B3nimo_01.jpg",
        "Museum": "Near Nîmes, France"
      },
      "Still Life with Eggs, Birds and Bronze Dishes, Fresco from Pompeii": {
        "id": 34,
        "Author": "Unknown",
        "Date": "1st century AD",
        "Description": "This fresco illustrates a still life scene with eggs, birds, and ornate bronze dishes, showcasing Roman daily life and luxury.",
        "Image": "https://upload.wikimedia.org/wikipedia/commons/1/1d/Kouros_An%C3%B3nimo_01.jpg",
        "Museum": "National Archaeological Museum, Naples"
      },
  "Colosseum Anon": {
    "id": 35,
    "Author": "Unknown",
    "Date": "1st century AD",
    "Description": "The iconic Colosseum, a monumental amphitheatre in the center of Rome, known for gladiatorial contests and public spectacles.",
    "Image": "https://upload.wikimedia.org/wikipedia/commons/5/53/Colosseum_in_Rome,_Italy_-_April_2007.jpg",
    "Museum": "Rome, Italy"
  },
  "House of Venus, Fresco from Pompeii": {
    "id": 36,
    "Author": "Unknown",
    "Date": "1st century AD",
    "Description": "A fresco from the House of Venus in Pompeii depicting the goddess Venus, showcasing the artistic elegance and detailed craftsmanship of Roman frescoes.",
    "Image": "https://upload.wikimedia.org/wikipedia/commons/1/1d/Kouros_An%C3%B3nimo_01.jpg",
    "Museum": "National Archaeological Museum, Naples"
  },
  "Relief of the Judgment of Paris": {
    "id": 37,
    "Author": "Unknown",
    "Date": "2nd century AD",
    "Description": "A marble relief depicting the mythological story of the Judgment of Paris, where Paris is tasked with selecting the most beautiful goddess leading to the events of the Trojan War.",
    "Image": "https://upload.wikimedia.org/wikipedia/commons/1/1d/Kouros_An%C3%B3nimo_01.jpg",
    "Museum": "Louvre Museum, Paris"
  },
  "Zeus or Jupiter of Smyrna": {
    "id": 38,
    "Author": "Unknown",
    "Date": "2nd century AD",
    "Description": "A grand statue of Zeus (Jupiter), originally from Smyrna, representing the king of the gods in classical mythology, noted for its imposing size and regal posture.",
    "Image": "https://upload.wikimedia.org/wikipedia/commons/1/1d/Kouros_An%C3%B3nimo_01.jpg",
    "Museum": "British Museum, London"
  },
  "Hercules Strangling a Serpent": {
    "id": 39,
    "Author": "Unknown",
    "Date": "2nd century AD",
    "Description": "A dynamic sculpture showing Hercules, the hero of classical mythology, in the act of strangling a serpent, symbolic of his divine strength and heroic deeds.",
    "Image": "https://upload.wikimedia.org/wikipedia/commons/1/1d/Kouros_An%C3%B3nimo_01.jpg",
    "Museum": "Vatican Museums, Rome"
  },
      "Aqueduct of Segovia": {
        "id": 40,
        "Author": "Roman Engineering",
        "Date": "1st century AD",
        "Description": "An ancient Roman aqueduct in Segovia, Spain, renowned for its remarkable state of preservation. It originally carried water from the Rio Frio to the city.",
        "Image": "https://upload.wikimedia.org/wikipedia/commons/1/1d/Kouros_An%C3%B3nimo_01.jpg",
        "Museum": "Segovia, Spain"
      },
      "Augustus of the Vatican Pio-Clementine Museum": {
        "id": 41,
        "Author": "Unknown",
        "Date": "1st century AD",
        "Description": "A statue of Emperor Augustus, housed in the Vatican's Pio-Clementine Museum, showcasing Augustan propaganda through art.",
        "Image": "https://upload.wikimedia.org/wikipedia/commons/1/1d/Kouros_An%C3%B3nimo_01.jpg",
        "Museum": "Vatican Museums, Rome"
      },
      "Venus or Aphrodite of Syracuse": {
        "id": 42,
        "Author": "Praxiteles",
        "Date": "4th century BC",
        "Description": "Attributed to the famed sculptor Praxiteles, this statue is a celebrated depiction of Aphrodite, highlighting classical Greek beauty and divinity.",
        "Image": "https://upload.wikimedia.org/wikipedia/commons/1/1d/Kouros_An%C3%B3nimo_01.jpg",
        "Museum": "Archaeological Museum of Syracuse, Italy"
      },
      "Trajan's Column": {
        "id": 43,
        "Author": "Apollodorus of Damascus",
        "Date": "113 AD",
        "Description": "A monumental column in Rome celebrating Emperor Trajan's victory in the Dacian Wars, famous for its spiral bas relief, which narrates the wars' history.",
        "Image": "https://upload.wikimedia.org/wikipedia/commons/1/1d/Kouros_An%C3%B3nimo_01.jpg",
        "Museum": "Rome, Italy"
      },
      "Jupiter or Zeus": {
        "id": 44,
        "Author": "Unknown",
        "Date": "Various",
        "Description": "Statues and sculptures representing Zeus (Jupiter), the king of the gods in Greek and Roman mythology, depicted as a figure of power and authority.",
        "Image": "https://upload.wikimedia.org/wikipedia/commons/1/1d/Kouros_An%C3%B3nimo_01.jpg",
        "Museum": "Various locations"
      },
      "Heracles or Hercules Farnese, Roman copy": {
        "id": 45,
        "Author": "Glykon of Athens",
        "Date": "3rd century AD",
        "Description": "A Roman copy of a lost original by Lysippos, this sculpture depicts Hercules in a moment of rest, holding the apples of the Hesperides.",
        "Image": "https://upload.wikimedia.org/wikipedia/commons/1/1d/Kouros_An%C3%B3nimo_01.jpg",
        "Museum": "National Archaeological Museum, Naples"
      },
      "Glykon of Athens, original by Lysippos": {
        "id": 46,
        "Author": "Lysippos",
        "Date": "4th century BC",
        "Description": "Known works by Lysippos include dynamic statues that introduced a new canon of proportions and a greater sense of movement to the depiction of the human body.",
        "Image": "https://upload.wikimedia.org/wikipedia/commons/1/1d/Kouros_An%C3%B3nimo_01.jpg",
        "Museum": "Various collections"
      },
      "Sarcophagus of the Twelve Labors of Hercules": {
        "id": 47,
        "Author": "Unknown",
        "Date": "2nd century AD",
        "Description": "A sarcophagus intricately carved with scenes from the twelve labors of Hercules, showcasing the hero's strength and divine challenges.",
        "Image": "https://upload.wikimedia.org/wikipedia/commons/1/1d/Kouros_An%C3%B3nimo_01.jpg",
        "Museum": "Vatican Museums, Rome"
      },
      "Athena Parthenos, recreation by Alan LeQuire": {
        "id": 48,
        "Author": "Alan LeQuire",
        "Date": "1990",
        "Description": "A modern full-scale recreation of the Athena Parthenos statue originally crafted by Phidias, placed in the Parthenon in Nashville, Tennessee.",
        "Image": "https://upload.wikimedia.org/wikipedia/commons/1/1d/Kouros_An%C3%B3nimo_01.jpg",
        "Museum": "Parthenon, Nashville, Tennessee"
      }
    }
  ]
}

}

            
}

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
