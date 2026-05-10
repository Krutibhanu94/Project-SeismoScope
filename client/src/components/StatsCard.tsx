import styles from "./StatsCard.module.css";

interface StatsCardProps {
  title: string
  value: number
}

function StatsCard({ title, value }: StatsCardProps) {
  return (
    <div className={styles.card}>
      <h3 className={styles.title}>{title}</h3>
      <strong className={styles.value}>{value}</strong>
    </div>
  )
}

export default StatsCard