from google.cloud import firestore

datanase = firestore.Client()

doc = datanase.collection("Batting_History").document("111")

print(doc.get().to_dict())