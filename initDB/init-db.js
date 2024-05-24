const dbName = process.env.MONGO_INITDB_DATABASE || 'meb_db';
const collectionName = 'deneme';

db.createUser({
  user: process.env.MONGO_INITDB_ROOT_USERNAME,
  pwd: process.env.MONGO_INITDB_ROOT_PASSWORD,
  roles: [
    {
      role: "readWrite",
      db: process.env.MONGO_INITDB_DATABASE
    }
  ]
});

const db = db.getSiblingDB(dbName);
db.createCollection(collectionName);
db[collectionName].insertOne({
  name: "Giray AKKAYA",
  email: "giray.akkaya@eba.gov.tr"
});