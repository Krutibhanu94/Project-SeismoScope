export const getStatistics = async () => {
  const response = await fetch('/api/statistics');
  if (!response.ok) {
    throw new Error('Failed to fetch statistics');
  }
  const data = await response.json();
  return {
    totalEarthquakes: data.total_earthquakes,
    averageMagnitude: data.average_magnitude,
    tsunamiCount: data.total_tsunamis,
    tsunamiRate: data.tsunami_rate,
  };
};

export const getEarthquakes = async () => {
  const response = await fetch('/api/earthquakes');
  if (!response.ok) {
    throw new Error('Failed to fetch earthquake data');
  }
  const data = await response.json();
  return data;
};  