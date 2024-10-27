"use client"
import React, { useEffect, useState } from 'react';
import Link from 'next/link';
import styles from './navbar.module.css';

const Navbar: React.FC = () => {
  const [isSticky, setIsSticky] = useState(false);

  useEffect(() => {
    const handleScroll = () => {
      const scrollY = window.scrollY;
      // Set sticky only when scrolling down a specific threshold to avoid excessive toggling
      if (scrollY > 50 && !isSticky) setIsSticky(true);
      else if (scrollY <= 50 && isSticky) setIsSticky(false);
    };

    window.addEventListener('scroll', handleScroll);

    return () => {
      window.removeEventListener('scroll', handleScroll);
    };
  }, [isSticky]);

  return (
    <nav className={`${styles.navbar} ${isSticky ? styles.sticky : ''}`}>
      <div className={styles.navLeft}>
        <Link href="/">
          <img src="/icons/fruitBowl.png" alt="Fruit Bowl" className={styles.logo} />
        </Link>
        <span className={styles.teamName}>VisionPay</span>
      </div>
    </nav>
  );
};

export default Navbar;
