# IOT-and-CLOUD
This project implements a secure system for collecting, storing, and managing player health data using wearable technology. A simulator generates real-time physiological data such as heart rate, temperature, and timestamp, which is sent to a Flask backend and stored in a Firebase Firestore database.  
 
The system ensures data security and privacy by applying role-based access control, where different users such as doctors, coaches, and analysts receive different levels of information. Doctors can access complete medical data, coaches receive only fatiguerelated insights, and analysts are provided with anonymized data using hashing techniques. 
 
 This approach protects sensitive information while still allowing useful analysis. Overall, the project demonstrates how cloud storage, secure access control, and data anonymization can be combined to build a scalable and privacy-preserving health monitoring system. 
 
