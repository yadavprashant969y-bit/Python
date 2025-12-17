"""Visualization module for task statistics using Matplotlib"""
import matplotlib.pyplot as plt

def plot_statistics(todo_list):
    """Display pie charts and statistics visualization"""
    stats = todo_list.get_statistics()
    
    # Create figure with subplots
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))
    fig.suptitle('TO-DO LIST STATISTICS', fontsize=16, fontweight='bold')
    
    # Chart 1: Pending vs Completed
    if stats['total'] > 0:
        statuses = [stats['pending'], stats['completed']]
        labels = [f"Pending\n({stats['pending']})", f"Completed\n({stats['completed']})"]
        colors = ['#FF9999', '#90EE90']
        
        axes[0].pie(statuses, labels=labels, colors=colors, autopct='%1.1f%%',
                   startangle=90, textprops={'fontsize': 11, 'weight': 'bold'})
        axes[0].set_title('Status Distribution', fontsize=12, fontweight='bold')
    else:
        axes[0].text(0.5, 0.5, 'No Tasks', ha='center', va='center', fontsize=14)
        axes[0].set_title('Status Distribution', fontsize=12, fontweight='bold')
    
    # Chart 2: Priority Distribution
    if stats['total'] > 0:
        priorities = [stats['high'], stats['medium'], stats['low']]
        labels = [f"High\n({stats['high']})", f"Medium\n({stats['medium']})", 
                 f"Low\n({stats['low']})"]
        colors = ['#FF6666', '#FFD700', '#87CEEB']
        
        axes[1].pie(priorities, labels=labels, colors=colors, autopct='%1.1f%%',
                   startangle=90, textprops={'fontsize': 11, 'weight': 'bold'})
        axes[1].set_title('Priority Distribution', fontsize=12, fontweight='bold')
    else:
        axes[1].text(0.5, 0.5, 'No Tasks', ha='center', va='center', fontsize=14)
        axes[1].set_title('Priority Distribution', fontsize=12, fontweight='bold')
    
    plt.tight_layout()
    plt.show()

def plot_completion_rate(todo_list):
    """Display completion rate chart"""
    stats = todo_list.get_statistics()
    
    fig, ax = plt.subplots(figsize=(10, 6))
    
    if stats['total'] > 0:
        completion_rate = (stats['completed'] / stats['total']) * 100
        remaining_rate = (stats['pending'] / stats['total']) * 100
        
        categories = ['Completed', 'Pending']
        values = [completion_rate, remaining_rate]
        colors = ['#90EE90', '#FF9999']
        
        bars = ax.bar(categories, values, color=colors, edgecolor='black', linewidth=2)
        ax.set_ylabel('Percentage (%)', fontsize=12, fontweight='bold')
        ax.set_title('Completion Rate', fontsize=14, fontweight='bold')
        ax.set_ylim(0, 100)
        
        # Add value labels on bars
        for bar in bars:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height,
                   f'{height:.1f}%', ha='center', va='bottom', fontweight='bold')
    else:
        ax.text(0.5, 0.5, 'No Tasks', ha='center', va='center', fontsize=14)
    
    plt.tight_layout()
    plt.show()
