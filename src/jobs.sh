for i in 1 2 4 6 8 10 
do
    python3 src/run_n_step_gridworld.py --policy="epsilon_greedy" \
        --max_steps=2000 --num_episodes=500 --num_trials=100 \
        --agent="n_step_sarsa" --n=$i --log_path="./four_rooms" --log_file="log_$i"
done
