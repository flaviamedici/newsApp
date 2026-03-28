# 📰 NewsApp

A simple and interactive **News Application** that allows users to view, explore, and interact with news content. The app includes **user authentication, location-based features, and messaging functionality**, making it more than just a basic news reader.

---

## 🚀 Features

- 🗞️ Browse latest news articles  
- 📍 Location-based functionality (GPS integration)  
- 👤 User session management (localStorage)  
- 💬 Messaging between users  
- 🧭 Dynamic UI updates  
- ⚡ Lightweight front-end app  

---

## 🛠️ Technologies Used

- JavaScript (Vanilla JS)
- HTML5
- CSS3
- Browser APIs:
  - Geolocation API
  - Local Storage

---

## 📂 Project Structure
newsApp/
│── index.html
│── style.css
│── script.js
│── assets/
│── README.md


---

## ⚙️ How It Works

1. Retrieves the current user from `localStorage`
2. Displays user information dynamically
3. Uses the Geolocation API to get user coordinates
4. Loads or simulates news content
5. Allows user interaction through messaging features

---

## 📍 Example Code

```javascript
navigator.geolocation.getCurrentPosition((position) => {
  const lat = position.coords.latitude;
  const lon = position.coords.longitude;

  console.log("Latitude:", lat);
  console.log("Longitude:", lon);
});
