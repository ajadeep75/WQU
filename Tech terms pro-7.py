# Cross Tab
import imports


data = pd.crosstab(
    index=<yourDataFrame>["group"],
    columns=<yourDataFrame>["admissionsQuiz"],
    normalize=False
)

# Probability
import statistical_summary


prob_65_or_fewer = scipy.stats.norm.cdf(
    group_size * 2,
    loc=sum_mean,
    scale=sum_std
)
prob_65_or_greater = 1 - prob_65_or_fewer

#Run exp
import imports
import connect
import mongo_instance


exp = Experiment(repo=client, db="yourDatabase", collection="yourCollection")
exp.reset_experiment()
result = exp.run_experiment(days=exp_days, assignment=True)

#Statistics power
import imports


chi_square_power = GofChisquarePower()
group_size = math.ceil(chi_square_power.solve_power(
    effect_size=0.5,  # medium --> 0.5; small --> 0.2; large --> 0.8
    alpha=0.05,
    power=0.8
))

#Statistical Summary
import imports
import load
import aggregate


mean = <ndf_Name>.describe()["mean"]
std = <ndf_Name>.describe()["std"]


# sum...
exp_days = <no_of_days>
sum_mean = mean * exp_days
sum_std = std * math.sqrt(exp_days)
