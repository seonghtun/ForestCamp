import React from "react"
// import React from "react"
import './App.css';
import DetailPage from "./Components/DetailPage"
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import NotFound from "./Components/NotFound";
import NaverReviewPage from "./Components/NaverReviewPage";
import Header from './Components/Header';
import Footer from './Components/Footer';
import styles from './App.module.css'
function App() {

  return (

    <BrowserRouter>
      <div className={styles.wrapper}>
        <Header />
        <div className={styles.content_wrapper}>
          <Routes>
            <Route path="camping">
              <Route path=":campId" element={<DetailPage />} />
              <Route path="reviews/:campName" element={<NaverReviewPage />} />
              <Route path="camping/*" element={<NotFound />} />
            </Route>
            <Route path="*" element={<NotFound />} />
          </Routes>
        </div>
        <Footer />
      </div>
    </BrowserRouter>

  );
}

export default App;
