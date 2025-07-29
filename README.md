# WBJEE Research Platform & College Predictor



Welcome to the ultimate research tool for West Bengal Joint Entrance Examination (WBJEE) aspirants. This platform is a comprehensive, serverless web application designed to help students predict their potential college placements and explore admission possibilities based on historical cutoff data.

**Live Application:** [**https://nobustark.github.io/wbjeecollegepredictor//**](https://nobustark.github.io/wbjeecollegepredictor/)

---

## ✨ Features

This platform is more than just a predictor. It's a full-featured research hub with three powerful tools:

*   **🎓 College Predictor:** Enter your General Merit Rank (GMR), Quota, and Category to get a personalized list of colleges you are likely to be admitted to, sorted by competitiveness.
*   **🏛️ College Explorer:** Select any college to view all its branches and their opening/closing ranks for every category. Perfect for researching specific institutes.
*   **🔭 Branch Explorer:** Select your dream branch (like Computer Science) to see a ranked list of all colleges that offer it, from the most to least competitive.
*   **🧠 Smart Guidance:** The app features a detailed guide to the WBJEE admission process and provides clear instructions on how to use each tool effectively.
*   **🚀 Blazing Fast & Serverless:** Built with modern, frontend-only technologies. All logic runs directly in your browser, making the experience instant and reliable. No backend, no server costs, no downtime.
*   **🎨 Sleek, Responsive UI:** A clean, dark-themed, mobile-friendly interface designed for an intuitive user experience.

---

## 🛠️ Tech Stack

This project was built from the ground up using fundamental web technologies, demonstrating a strong understanding of frontend development and data handling.

*   **Frontend:** HTML5, CSS3, Vanilla JavaScript (ES6+)
*   **Data Handling:** JavaScript for all filtering, sorting, and prediction logic. The database is a static `database.js` file converted from CSV.
*   **Development Tools:** Python with Pandas for initial data cleaning and CSV-to-JSON conversion.
*   **Deployment:** Hosted on **GitHub Pages** for fast, free, and reliable static site hosting.

---

## 🚀 How It Was Built

This project began as a full-stack application with a Python (Flask) backend deployed on Render. However, to enhance performance, reduce complexity, and eliminate hosting costs, it was strategically refactored into a fully **serverless, frontend-only application**.

1.  **Data Processing:** The initial raw data was scraped and cleaned using Python and the Pandas library.
2.  **Database Creation:** A Python script converted the cleaned CSV data into a static `database.js` file, which acts as the local database for the application.
3.  **Core Logic:** All prediction, filtering, and exploration logic was rewritten in Vanilla JavaScript, running entirely on the client-side.
4.  **UI/UX:** The user interface was built with semantic HTML and styled with modern CSS, including Flexbox and Grid, for a responsive and intuitive layout.

This architectural choice makes the application incredibly efficient, scalable, and easy to maintain.

---

## ✍️ About the Creator

This project was created by **Sk Nabab**, a pre-final year Chemical Engineering student at Jadavpur University.

*   **Email:** [nobustark@gmail.com](mailto:nobustark@gmail.com)
*   **LinkedIn:** [https://www.linkedin.com/in/nobuparker/] <!-- Add your LinkedIn URL here! -->

Feel free to reach out with any feedback, questions, or collaboration opportunities!
