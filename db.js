const {MongoClient} = require('mongodb');

const uri = "mongodb://localhost:27017";
const client = new MongoClient(uri);

async function connect(){
    try{
        await client.connect();
        client.db('tienda');
        console.log('conectado a mongodb')  
    }catch (error){
      console.error("Error al conectar a MongoDB", error);
    };
 
}

module.exports = { connect };