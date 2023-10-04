import react from "react";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import styles from "./App.module.css";
import Header from "./Components/public/Header";
import Footer from "./Components/public/Footer";
import Searchpage from "./Components/search/Searchpage";
import Content from "./Components/main/Content";
import CampingSupplies from "./Components/equipment/CampingSupplies";
import NaverReviewPage from "./Components/camp/NaverReviewPage";
import CampDetailPage from "./Components/camp/CampDetailPage";
import NotFound from "./Components/camp/NotFound";
import Login from "./Components/login/Login";
import Mypage from "./Components/login/Mypage";


function App() {

  return (
    <BrowserRouter>
      <div className={styles.wrapper}>
        <Header />
        <div className={styles.content_wrapper}>
          <Routes>
            <Route element={<CampingSupplies />} path="/equipment/:id" />
            {<Route path="/" element={<Content />} />}
            {<Route path="/search" element={<Searchpage />} />}
            <Route path="/camping">
              <Route path="reviews/:campName" element={<NaverReviewPage />} />
              <Route path=":campId" element={<CampDetailPage />} />
            </Route>
            <Route path="/login" element={<Login />} />
            <Route path="/mypage" element={<Mypage />} />
            <Route path="/*" element={<NotFound />} />
          </Routes>
        </div>
        <Footer />
      </div>
    </BrowserRouter>
  );
}

export default App;
