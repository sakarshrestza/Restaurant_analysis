import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

# Menu Configuration (same as before)
menu_items = {
    'Veg Thali': ['Veg', 180, 0.95, None],
    'Chicken Thali': ['Non-Veg', 220, 0.9, None],
    'Paneer Butter Masala': ['Veg', [120, 210], 0.9, 'half/full'],
    'Butter Chicken': ['Non-Veg', [140, 240], 0.95, 'half/full'],
    'Dal Makhani': ['Veg', [100, 190], 1, 'half/full'],
    'Rajma Chawal': ['Veg', [90, 170], 0.7, 'half/full'],
    'Chole Bhature': ['Veg', [90, 160], 0.72, 'half/full'],
    'Shahi Paneer': ['Veg', [130, 220], 0.9, 'half/full'],
    'Kadhai Paneer': ['Veg', [120, 200], 0.75, 'half/full'],
    'Kadhai Chicken': ['Non-Veg', [140, 230], 0.77, 'half/full'],
    'Chicken Tikka': ['Non-Veg', [130, 210], 0.8, 'half/full'],
    'Paneer Tikka': ['Veg', [120, 190], 0.78, 'half/full'],
    'Chicken Tikka Masala': ['Non-Veg', [140, 240], 0.81, 'half/full'],
    'Chicken Curry': ['Non-Veg', [120, 200], 0.75, 'half/full'],
    'Paneer Tikka Masala': ['Veg', [130, 220], 0.79, 'half/full'],
    'Paneer Lababdar': ['Veg', [140, 230], 0.76, 'half/full'],
    'Paneer Do Pyaza': ['Veg', [130, 210], 0.74, 'half/full'],
    'Veg Biryani': ['Veg', [110, 180], 0.85, 'half/full'],
    'Chicken Biryani': ['Non-Veg', [140, 220], 0.88, 'half/full'],
    'Fried Rice': ['Veg', [90, 150], 0.7, 'half/full'],
    'Butter Naan': ['Veg', 40, 0.7, None],
    'Tandoori Roti': ['Veg', 30, 0.85, None],
    'Tawa Roti': ['Veg', 25, 0.8, None],
    'Rumali Roti': ['Veg', 35, 0.82, None],
    'Stuffed Paratha': ['Veg', 60, 0.75, None],
    'Tandoori Chicken': ['Non-Veg', [180, 280], 1, 'half/full'],
    'Chicken Manchurian': ['Non-Veg', [110, 180], 0.5, 'half/full'],
    'Chilli Paneer': ['Veg', [100, 170], 0.8, 'half/full'],
    'Chilli Chicken': ['Non-Veg', [120, 190], 0.7, 'half/full'],
    'Egg Noodles': ['Non-Veg', [100, 160], 0.6, 'half/full'],
    'Chicken Noodles': ['Non-Veg', [110, 170], 0.7, 'half/full'],
    'Idli (2 pcs)': ['Veg', 80, 0.6, None],
    'Plain Dosa': ['Veg', 100, 0.5, None],
    'Masala Dosa': ['Veg', 120, 0.5, None],
    'Pyaaz Dosa': ['Veg', 110, 0.5, None],
    'Mix Dosa': ['Veg', 130, 0.5, None],
    'Rawa Dosa': ['Veg', 140, 0.5, None],
    'Paneer Dosa': ['Veg', 150, 0.72, None],
    'Cold Drink (500ml)': ['Veg', 60, 0.9, None],
    'Sweet Lassi': ['Veg', 70, 0.75, None],
    'Water Bottle': ['Veg', 20, 0.95, None],
    'Gulab Jamun': ['Veg', 60, 0.85, None],
    'Kheer': ['Veg', 70, 0.8, None],
    'Gajar Ka Halwa': ['Veg', 80, 0.7, None]
}

locations = {
    'Sarita Vihar': {'weight': 0.1, 'distance_km': 1.0},
    'Jasola': {'weight': 0.09, 'distance_km': 1.2},
    'Jasola Vihar': {'weight': 0.09, 'distance_km': 1.3},
    'Madanpur Khadar Village': {'weight': 0.08, 'distance_km': 1.5},
    'JJ Colony (Madanpur Khadar)': {'weight': 0.08, 'distance_km': 1.6},
    'Okhla Phase 1': {'weight': 0.07, 'distance_km': 2.0},
    'Okhla Industrial Area': {'weight': 0.07, 'distance_km': 2.2},
    'Ali Vihar': {'weight': 0.06, 'distance_km': 2.3},
    'Kalindi Kunj': {'weight': 0.06, 'distance_km': 2.5},
    'Badarpur': {'weight': 0.05, 'distance_km': 3.0},
    'Shaheen Bagh': {'weight': 0.05, 'distance_km': 3.2},
    'New Friends Colony': {'weight': 0.04, 'distance_km': 4.0},
    'Sukhdev Vihar': {'weight': 0.04, 'distance_km': 4.2},
    'Jamia Nagar': {'weight': 0.03, 'distance_km': 4.5},
    'Govindpuri': {'weight': 0.03, 'distance_km': 5.0},
    'Tughlakabad': {'weight': 0.02, 'distance_km': 5.5},
    'Jasola East': {'weight': 0.02, 'distance_km': 1.4},
    'Jasola West': {'weight': 0.02, 'distance_km': 1.4},
    'Khizrabad': {'weight': 0.02, 'distance_km': 2.8},
    'Sangam Vihar': {'weight': 0.02, 'distance_km': 6.0},
    'Kalkaji': {'weight': 0.02, 'distance_km': 5.0},
    'Nehru Place': {'weight': 0.01, 'distance_km': 5.2},
    'Saidulajab': {'weight': 0.01, 'distance_km': 3.5},
    'Okhla Phase 2': {'weight': 0.01, 'distance_km': 2.1},
    'Okhla Phase 3': {'weight': 0.01, 'distance_km': 2.3},
    'Zakir Nagar': {'weight': 0.01, 'distance_km': 4.3},
    'Masoodpur': {'weight': 0.01, 'distance_km': 3.8},
    'Bishamber Nagar': {'weight': 0.01, 'distance_km': 2.4},
    'Jamia Millia Islamia Campus Area': {'weight': 0.01, 'distance_km': 4.4}
}

num_customers = 1000
max_orders_per_customer = 5# limit max orders per customer to avoid one customer ordering too many times

customers = [{'customer_id': f'C{i + 10001}', 'orders_placed': 0} for i in range(num_customers)]
start_date = datetime(2024, 9, 6)
end_date = datetime(2024, 12, 20)
date_range = pd.date_range(start_date, end_date)

item_weights = [item[2] if isinstance(item[2], (int, float)) else np.mean(item[2]) for item in menu_items.values()]
total_weight = sum(item_weights)
item_weights = [w / total_weight for w in item_weights]

location_weights = [loc['weight'] for loc in locations.values()]
total_loc_weight = sum(location_weights)
location_weights = [w / total_loc_weight for w in location_weights]

orders = []
order_id = 10000
target_orders = 2000

repeat_orders = 0
new_orders = 0
used_customers = set()

target_repeat_ratio = 0.35  # aim for 35% repeat orders

print("🔃 Starting order simulation...")

for date in date_range:
    if len(orders) >= target_orders:
        break
    weekday = date.weekday()
    base_orders = random.randint(100, 150) if weekday in [4, 5, 6] else random.randint(30, 80)
    base_orders = int(base_orders * (1.2 if date.month >= 11 else 1.0))
    base_orders = min(base_orders, target_orders - len(orders))

    for _ in range(base_orders):
        # Decide if repeat order or new order based on current ratio and target ratio
        total_so_far = repeat_orders + new_orders
        if total_so_far == 0:
            choose_repeat = False
        else:
            current_repeat_ratio = repeat_orders / total_so_far
            choose_repeat = current_repeat_ratio < target_repeat_ratio

        if choose_repeat and used_customers:
            # pick repeat customer with orders < max_orders_per_customer
            repeat_candidates = [c for c in customers if c['customer_id'] in used_customers and c['orders_placed'] < max_orders_per_customer]
            if not repeat_candidates:
                choose_repeat = False

        if choose_repeat:
            customer = random.choice(repeat_candidates)
            repeat_orders += 1
        else:
            # pick a new customer who hasn't ordered yet
            new_candidates = [c for c in customers if c['orders_placed'] == 0]
            if not new_candidates:
                # fallback: all customers have ordered, pick from all with less than max orders
                new_candidates = [c for c in customers if c['orders_placed'] < max_orders_per_customer]
            customer = random.choice(new_candidates)
            new_orders += 1
            used_customers.add(customer['customer_id'])

        customer['orders_placed'] += 1
        customer_id = customer['customer_id']

        customer_type = random.choices(['Offline', 'Online'], weights=[0.4, 0.6])[0]
        if customer_type == 'Offline':
            customer_location = 'Restaurant'
            distance_km = 0
        else:
            customer_location = random.choices(list(locations.keys()), weights=location_weights, k=1)[0]
            distance_km = locations[customer_location]['distance_km']

        is_dinner = random.random() > 0.6
        hour = random.choice([19, 20, 21]) if is_dinner else random.choice([12, 13])
        minute = random.choice([0, 15, 30, 45])
        order_time = datetime(date.year, date.month, date.day, hour, minute).time()

        order_id += 1
        discount = 'yes' if random.random() < 0.3 else 'no'

        num_items = random.choices([1, 2, 3], weights=[0.5, 0.3, 0.2])[0]
        for _ in range(num_items):
            item_name, item_data = random.choices(list(menu_items.items()), weights=item_weights, k=1)[0]

            # Seasonal item
            if item_name == 'Gajar Ka Halwa' and date.month not in [11, 12, 1]:
                continue

            if item_data[3] == 'half/full':
                portion = random.choices(['half', 'full'], weights=[0.4, 0.6])[0]
                item_price = item_data[1][0] if portion == 'half' else item_data[1][1]
            else:
                portion = None
                item_price = item_data[1]

            quantity = 1
            if item_name in ['Butter Naan', 'Tandoori Roti', 'Rumali Roti']:
                quantity = random.choices([1, 2, 3], weights=[0.6, 0.3, 0.1])[0]

            orders.append({
                'order_id': order_id,
                'customer_id': customer_id,
                'item_name': item_name,
                'item_type': item_data[0],
                'portion_size': portion,
                'item_price': item_price,
                'item_qty': quantity,
                'transaction_amt': item_price * quantity,
                'transaction_type': random.choices(['Cash', 'Digital'], weights=[0.3, 0.7])[0],
                'time': order_time,
                'date': date.date(),
                'customer_type': customer_type,
                'customer_location': customer_location,
                'distance_km': distance_km,
                'discount': discount,
                'order_cancelled': 'no'
            })

        if len(orders) >= target_orders:
            break

# Create dataframe
df = pd.DataFrame(orders)
weekday_map = {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday', 4: 'Friday', 5: 'Saturday', 6: 'Sunday'}
df['weekday'] = df['date'].apply(lambda x: weekday_map[x.weekday()])

# Determine cancellations
def determine_cancellation(row):
    if row['customer_type'] == 'Offline':
        return 'no'
    base_prob = 0.05 + row['distance_km'] * 0.05
    if row['discount'] == 'no':
        base_prob += 0.15
    if row['distance_km'] > 5:
        base_prob += 0.2
    return 'yes' if random.random() < min(base_prob, 0.7) else 'no'

df['order_cancelled'] = df.apply(determine_cancellation, axis=1)

# Save CSV
df.to_csv('restaurant_orders_final.csv', index=False)

# Calculate repeat rate
unique_customers = df['customer_id'].nunique()
total_orders = df['order_id'].nunique()
repeat_rate = round((total_orders - unique_customers) / total_orders * 100, 2)

print("✅ Dataset generation complete!")
print(f"📦 Total rows: {len(df)}")
print(f"🔁 Repeat customer rate: {repeat_rate}%")
print("📊 Sample data:\n", df.sample(5))
