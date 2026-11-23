# Task 3: Simple Load Balancer Simulation

## Setup
```bash
pip install -r requirements.txt
```

## Running the Simulation
Start each backend server and the load balancer in separate terminals:
```bash
python server1.py
python server2.py
python server3.py
python load_balancer.py
```

## Testing Round-Robin Distribution
```bash
for i in {1..6}; do curl http://127.0.0.1:5000/; done
```
Or run:
```bash
python test_lb.py
```
