import React, { useState } from 'react';
import Banners from '../public/Banners';
import styles from './Searchpage.module.css';
import SearchForm from './SearchForm';
import Card from './Card';
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faSliders, faTimes } from "@fortawesome/free-solid-svg-icons";
import Checkbox from './Checkbox';


import {
    placeDatas,
    placetheme,
    equipmentCategori,
    tentCategoro,
    tentSupplies,
    tarp,
    campingMat,
    sleepingBag,
    chair
} from './checkdata';

const Searchpage = (props) => {
    const [eqdata, setEqdata] = useState(false);
    const [isOpen, setMenu] = useState(true);
    const [selectedPlaceDataIndex, setSelectedPlaceDataIndex] = useState([]);
    const [selectedEquipmentCategoryIndex, setSelectedEquipmentCategoryIndex] = useState([]);

    const toggleMenu = () => {
        setMenu(isOpen => !isOpen);
    }

    const handlePlaceDataChange = (index) => {
        if (selectedPlaceDataIndex.includes(index)) {
            setSelectedPlaceDataIndex(selectedPlaceDataIndex.filter(i => i !== index));
        } else {
            setSelectedPlaceDataIndex([...selectedPlaceDataIndex, index]);
        }
    };

    const handleEquipmentCategoryChange = (index) => {
        if (selectedEquipmentCategoryIndex.includes(index)) {
            setSelectedEquipmentCategoryIndex(selectedEquipmentCategoryIndex.filter(i => i !== index));
        } else {
            setSelectedEquipmentCategoryIndex([...selectedEquipmentCategoryIndex, index]);
        }
    };

    return (
        <div className={styles.wrap}>
            <SearchForm />
            <div className={styles.modal}>
                <p className={`${styles.modalText}`} onClick={() => toggleMenu()} >필터
                    <FontAwesomeIcon className={styles.icon_spacing} icon={faSliders} />
                </p>
                <div className={`${styles.box} ${isOpen ? styles.show_menu : styles.hide_menu}`}>
                    <div className={styles.boxHeader}>
                        <h2 className={styles.boxtxt}>필 터</h2>
                        <FontAwesomeIcon className={styles.icon_spacing_b} icon={faTimes} onClick={() => toggleMenu()} />
                    </div>
                    <div className={styles.checkBox}>
                        <br />
                        <h2 className={styles.boxtxt}>숙소 종류</h2>
                        {placeDatas.map((placeData, index) => (
                            <Checkbox key={`place-${index}`} onChange={() => handlePlaceDataChange(index)}>
                                <span>{placeData}</span>
                            </Checkbox>
                        ))}

                        <br />
                        <br />

                        <h2 className={styles.boxtxt}>숙소 키워드 </h2>
                        <div>
                            {placetheme.map((themeItem, index) =>
                            (<Checkbox key={`placetheme-${index}`}>
                                <span>{themeItem}</span>
                            </Checkbox>)
                            )}
                        </div>

                        <h2 className={styles.boxtxt}>장비</h2>
                        {equipmentCategori.map((category, index) =>
                        (<Checkbox key={`category-${index}`} onChange={() => handleEquipmentCategoryChange(index)}>
                            <span>{category}</span>
                        </Checkbox>)
                        )}


                        {selectedEquipmentCategoryIndex.includes(0) && (
                            <>
                                {/* tentCategoro */}
                                {tentCategoro.map((item, index) =>
                                (<Checkbox key={`tentCategoro-${index}`}>
                                    <span>{item}</span>
                                </Checkbox>)
                                )}

                                {/* tentSupplies */}
                                {tentSupplies.map((item, index) =>
                                (<Checkbox key={`tentSupplies-${index}`}>
                                    <span>{item}</span>
                                </Checkbox>)
                                )}

                                {/* tarp */}
                                {tarp.map((item, index) =>
                                (<Checkbox key={`tarp-${index}`}>
                                    <span>{item}</span>
                                </Checkbox>)
                                )}


                                {campingMat.map((item, index) => (
                                    <Checkbox key={`Mat-${index}`}>
                                        <span>{item}</span>
                                    </Checkbox>
                                ))}



                            </>
                        )}
                    </div>

                </div>

            </div>

            <Card eqdata={eqdata} />
            <Banners />
        </div>

    );
};

export default Searchpage;
