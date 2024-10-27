import React from 'react';
import Link from 'next/link';
import styles from './navbar.module.css';

const Navbar: React.FC = () => {
    return (
        <nav className={styles.navbar}>
            <div className={styles.navLeft}>
                <Link href="/" passHref>
                    <img src="/icons/fruitBowl.png" alt="Fruit Bowl" className={styles.logo} />
                </Link>
                <span className={styles.teamName}>VisionPay</span>
            </div>
            <div className={styles.navRight}>
                <Link href="/about" className={styles.navLink}>About Us</Link>
            </div>
        </nav>
    );
};

export default Navbar;
