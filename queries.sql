-- Which rural counties are RISING - the most concerning ones
SELECT county, incidence_rate, avg_annual_count, trend
FROM county_incidence
WHERE rural_urban = 'Rural' AND trend = 'rising'
ORDER BY incidence_rate DESC;

-- Counties with highest case burden (rate x count combined view)
SELECT county, rural_urban, incidence_rate, avg_annual_count,
ROUND((incidence_rate * avg_annual_count) / 100, 2) AS burden_score
FROM county_incidence
ORDER BY burden_score DESC
LIMIT 15;

-- How does Iowa's overall rate compare broken down by rural urban
SELECT 
    rural_urban,
    COUNT(*) as county_count,
    ROUND(AVG(incidence_rate), 2) as avg_rate,
    ROUND(MAX(incidence_rate), 2) as highest_rate,
    ROUND(MIN(incidence_rate), 2) as lowest_rate
FROM county_incidence
GROUP BY rural_urban;


-- Counties significantly above state average of 498.8
SELECT county, rural_urban, incidence_rate, trend,
ROUND(incidence_rate - 498.8, 2) AS above_state_average
FROM county_incidence
WHERE incidence_rate > 498.8
ORDER BY above_state_average DESC;