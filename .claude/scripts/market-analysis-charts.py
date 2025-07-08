#!/usr/bin/env python3
"""
Market Analysis Data Visualization Script
Generates charts and graphs from market research data
"""

import json
import os
from datetime import datetime

def generate_market_size_chart():
    """Generate market size projection data for charting"""
    data = {
        "title": "Global Software Development Market Projection",
        "years": [2024, 2025, 2026, 2027, 2028, 2029, 2030],
        "market_size": [737, 824, 925, 1040, 1170, 1310, 1470],
        "ai_segment": [122, 156, 201, 259, 335, 397, 467],
        "outsourcing": [92.5, 180, 350, 442, 608, 739, 846]
    }
    return data

def generate_adoption_metrics():
    """Generate AI adoption metrics"""
    data = {
        "developer_tools": {
            "ChatGPT": 82,
            "GitHub Copilot": 44,
            "Google Gemini": 22,
            "Claude": 18,
            "Tabnine": 12,
            "Codeium": 8
        },
        "enterprise_adoption": {
            "2023": 55,
            "2024": 78,
            "2025": 89,
            "2026": 94,
            "2027": 97
        }
    }
    return data

def generate_regional_analysis():
    """Generate regional market analysis"""
    data = {
        "regions": {
            "North America": {
                "2024_size": 337,
                "2030_size": 583,
                "cagr": 11.2,
                "market_share": 45.8
            },
            "Europe": {
                "2024_size": 185,
                "2030_size": 295,
                "cagr": 12.5,
                "market_share": 25.2
            },
            "Asia Pacific": {
                "2024_size": 157,
                "2030_size": 406,
                "cagr": 19.4,
                "market_share": 21.3
            },
            "Rest of World": {
                "2024_size": 58,
                "2030_size": 116,
                "cagr": 15.0,
                "market_share": 7.7
            }
        }
    }
    return data

def generate_cost_comparison():
    """Generate cost comparison data"""
    data = {
        "traditional_development": {
            "US Team": {"monthly": 107500, "per_project": 322500},
            "Europe Team": {"monthly": 70000, "per_project": 210000},
            "India Team": {"monthly": 23650, "per_project": 71000},
            "Vietnam Team": {"monthly": 23700, "per_project": 71100}
        },
        "ai_swarm": {
            "daily_range": [100, 500],
            "monthly_range": [3000, 15000],
            "per_project_range": [200, 1500]
        },
        "cost_reduction_factor": {
            "time_based": [8, 35],  # 8-35x
            "per_project": [47, 1612]  # 47-1,612x
        }
    }
    return data

def generate_customer_segments():
    """Generate customer segment analysis"""
    data = {
        "segments": {
            "Startups": {
                "size": "90M globally",
                "budget": "$0-50K/year",
                "pain_points": ["Funding constraints", "Speed to market", "Talent shortage"],
                "adoption_barrier": "Lowest",
                "priority": 1
            },
            "SMBs": {
                "size": "400M globally",
                "budget": "$50K-500K/year",
                "pain_points": ["Digital transformation", "Cost control", "Scaling"],
                "adoption_barrier": "Low-Medium",
                "priority": 2
            },
            "Enterprises": {
                "size": "1M+ globally",
                "budget": "$10M+/year",
                "pain_points": ["Legacy systems", "Security", "Compliance"],
                "adoption_barrier": "Highest",
                "priority": 3
            },
            "Agencies": {
                "size": "500K+ globally",
                "budget": "$1M-50M/year",
                "pain_points": ["Project estimation", "Resource allocation", "Margins"],
                "adoption_barrier": "Medium",
                "priority": 2
            }
        }
    }
    return data

def generate_revenue_projections():
    """Generate revenue projection scenarios"""
    data = {
        "conservative": {
            "2025": 5,
            "2026": 35,
            "2027": 125,
            "2028": 280,
            "2029": 450,
            "2030": 650
        },
        "realistic": {
            "2025": 15,
            "2026": 75,
            "2027": 200,
            "2028": 450,
            "2029": 800,
            "2030": 1200
        },
        "aggressive": {
            "2025": 25,
            "2026": 150,
            "2027": 500,
            "2028": 1000,
            "2029": 1800,
            "2030": 2500
        }
    }
    return data

def save_data(filename, data):
    """Save data to JSON file"""
    output_dir = "business-documents/market-analysis/data"
    os.makedirs(output_dir, exist_ok=True)

    filepath = os.path.join(output_dir, f"{filename}.json")
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=2)
    print(f"Saved: {filepath}")

def main():
    """Generate all market analysis data files"""
    print("Generating market analysis data files...")
    print(f"Timestamp: {datetime.now().isoformat()}")
    print("-" * 50)

    # Generate and save all data
    datasets = {
        "market_size": generate_market_size_chart(),
        "adoption_metrics": generate_adoption_metrics(),
        "regional_analysis": generate_regional_analysis(),
        "cost_comparison": generate_cost_comparison(),
        "customer_segments": generate_customer_segments(),
        "revenue_projections": generate_revenue_projections()
    }

    for name, data in datasets.items():
        save_data(name, data)

    # Generate summary statistics
    summary = {
        "generated_at": datetime.now().isoformat(),
        "total_addressable_market": 737,  # Billion USD
        "serviceable_addressable_market": 250,
        "serviceable_obtainable_market": 50,
        "initial_target_market": 5,
        "key_metrics": {
            "cost_reduction": "47-1,612x per project",
            "speed_improvement": "Up to 50x faster",
            "quality_guarantee": "80%+ test coverage",
            "availability": "24/7/365"
        }
    }

    save_data("summary", summary)

    print("-" * 50)
    print("✅ Data generation complete!")
    print("\nNext steps:")
    print("1. Use the JSON files for creating visualizations")
    print("2. Import into BI tools for interactive dashboards")
    print("3. Update quarterly with new market data")

if __name__ == "__main__":
    main()
