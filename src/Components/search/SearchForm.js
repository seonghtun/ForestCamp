import React from 'react';
import styles from './SearchForm.module.css';
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faMagnifyingGlass } from "@fortawesome/free-solid-svg-icons"

const SearchForm = () => {
    const handleOnKeyPress = (e)=>{
        if(e.key === 'Enter'){
            console.log('press Enter')
        }
    }

    return (
        <form className={styles.search}>
            <input
                type='text'
                placeholder='검색할 키워드를 입력해주세요'
                className={styles.search_bar}
                onChange={handleOnKeyPress}
            />
            <button className={styles.enterbtn} type='submit'>
                <FontAwesomeIcon className={styles.icon_spacing} icon={faMagnifyingGlass} />
            </button>
        </form>
    );
};

export default SearchForm;