import mongoose  from "mongoose";
const connectDB = async()=>{
    const MONGO_URL='mongodb://localhost:27017';
    try{
        const conn = await mongoose.connect(MONGO_URL)
        // const conn = await mongoose.connect(process.env.MONGO_URL)
        console.log(`Connected to MongoDb Database ${conn.connection.host}`)
    }catch(error)
    {
        console.log(`Error in MongoDb ${error}`)
    }
    
}
export default connectDB;