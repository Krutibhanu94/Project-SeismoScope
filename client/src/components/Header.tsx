import styles from "./Header.module.css";

function Header() {
  return (
    <header className={styles.header}>
      <h1 className={styles.title}>SeismoScope</h1>
      <p className={styles.subtitle}>
        Exploring earthquake and tsunami patterns worldwide
      </p>
    </header>
  );
}

export default Header;