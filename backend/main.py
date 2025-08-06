"""
        Main execution script for the Tower Jump Analyzer backend.
        Coordinates data loading, cleaning, analysis, and report export.
    """
    
from loader import load_data
from cleaner import clean_data
from analyzer import analyze_intervals
from report import export_report

def main():
    try:
        print("Loading data ...")
        df = load_data()
    
        print("Cleaning and organizing data ...")
        df_clean = clean_data(df)
        
        print("Analyzing intervals ...")
        df_result = analyze_intervals(df_clean)
        
        print("Exporting report ...")
        export_report(df_result)
        
        print("Process completed.")
    except FileNotFoundError as e:
        print(f"File not found: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()
