import React from 'react';
import { useParams } from 'react-router-dom';
import NaverReviewComponent from "./NaverReviews";



const NaverReviewPage = () => {
    let { campName } = useParams();
    const url = `/v1/search/blog.json?query=${campName}&display=50`

    return (
        <div >
            <h1>Reviews</h1>
            <NaverReviewComponent url={url} />
        </div>
    );
};

export default NaverReviewPage;