// Task 2: use database
use bookstore

// Task 3: insert first author
db.authors.insertOne({
  "name": "Jane Austen",
  "nationality": "British",
  "bio": {
    "short": "English novelist known for novels about the British landed gentry.",
    "long": "Jane Austen was an English novelist whose works critique and comment upon the British landed gentry at the end of the 18th century. Her most famous novels include Pride and Prejudice, Sense and Sensibility, and Emma."
  }
})

// Task 4: update to add birthday
db.authors.updateOne(
  { name: "Jane Austen" },
  { $set: { birthday: "1775-12-16" } }
)

// Task 5: insert four more authors
db.authors.insertMany([
{
  "name": "Mark Twain",
  "nationality": "American",
  "bio": {
    "short": "American writer known for humor.",
    "long": "Mark Twain was an American writer best known for The Adventures of Tom Sawyer and Adventures of Huckleberry Finn."
  },
  "birthday": "1835-11-30"
},
{
  "name": "Charles Dickens",
  "nationality": "British",
  "bio": {
    "short": "English novelist and social critic.",
    "long": "Charles Dickens created some of the world's best known fictional characters."
  },
  "birthday": "1812-02-07"
},
{
  "name": "Gabriel Garcia Marquez",
  "nationality": "Colombian",
  "bio": {
    "short": "Colombian novelist known for magical realism.",
    "long": "Gabriel Garcia Marquez wrote One Hundred Years of Solitude."
  },
  "birthday": "1927-03-06"
},
{
  "name": "Haruki Murakami",
  "nationality": "Japanese",
  "bio": {
    "short": "Japanese writer known for surreal fiction.",
    "long": "Haruki Murakami blends surrealism with modern themes."
  },
  "birthday": "1949-01-12"
}
])

// Task 6: total count
db.authors.countDocuments({})

// Task 7: British authors sorted by name
db.authors.find({ nationality: "British" }).sort({ name: 1 })
