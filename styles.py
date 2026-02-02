"""
Styles Module
Contains CSS styling for the Streamlit application
"""


def get_custom_css():
    """
    Returns custom CSS for modern glassmorphic design
    
    Returns:
        str: CSS styling code
    """
    return """
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
        
        /* Main background */
        .stApp {
            background: #000000;
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
        }
        
        /* Remove default padding */
        .block-container {
            padding-top: 2rem;
            padding-bottom: 2rem;
        }
        
        /* Glassmorphic containers */
        .glass-container {
            background: rgba(0, 20, 0, 0.4);
            backdrop-filter: blur(20px) saturate(180%);
            -webkit-backdrop-filter: blur(20px) saturate(180%);
            border-radius: 16px;
            border: 1px solid rgba(0, 255, 0, 0.15);
            padding: 24px;
            box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
            margin: 10px 0;
        }
        
        /* Headers */
        h1 {
            color: #ffffff !important;
            font-weight: 700 !important;
            letter-spacing: -0.5px;
            margin-bottom: 0.5rem !important;
        }
        
        h2, h3 {
            color: #d0d0d0 !important;
            font-weight: 600 !important;
            letter-spacing: -0.3px;
            margin-top: 2rem !important;
            margin-bottom: 1rem !important;
        }
        
        /* Text */
        p, div, span, label {
            color: #a0a0a0 !important;
            font-weight: 400;
        }
        
        /* Metric cards */
        [data-testid="stMetricValue"] {
            color: #ffffff !important;
            font-size: 2.5rem !important;
            font-weight: 600 !important;
            text-shadow: none !important;
        }
        
        [data-testid="stMetricLabel"] {
            color: #888888 !important;
            font-size: 0.875rem !important;
            font-weight: 500 !important;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }
        
        [data-testid="stMetricDelta"] {
            color: #00ff00 !important;
        }
        
        [data-testid="metric-container"] {
            background: rgba(0, 20, 0, 0.3);
            backdrop-filter: blur(20px);
            border: 1px solid rgba(0, 255, 0, 0.15);
            border-radius: 12px;
            padding: 20px;
            box-shadow: 0 4px 16px rgba(0, 0, 0, 0.3);
        }
        
        /* Buttons */
        .stButton>button {
            background: #00ff00 !important;
            color: #000000 !important;
            border: none;
            border-radius: 8px;
            padding: 12px 28px;
            font-weight: 600;
            font-size: 1rem;
            box-shadow: 0 4px 16px rgba(0, 255, 0, 0.3);
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
            letter-spacing: 0.3px;
        }
        
        .stButton>button p {
            color: #000000 !important;
        }
        
        .stButton>button:hover {
            background: #00cc00 !important;
            box-shadow: 0 6px 24px rgba(0, 255, 0, 0.5);
            transform: translateY(-2px);
        }
        
        .stButton>button:active {
            transform: translateY(0px);
        }
        
        /* Progress bar */
        .stProgress > div > div > div {
            background: #00ff00;
            box-shadow: 0 0 16px rgba(0, 255, 0, 0.6);
        }
        
        .stProgress > div > div {
            background: rgba(255, 255, 255, 0.05);
            border-radius: 10px;
        }
        
        /* File uploader */
        [data-testid="stFileUploader"] {
            background: rgba(0, 20, 0, 0.3);
            backdrop-filter: blur(20px);
            border: 2px dashed rgba(0, 255, 0, 0.3);
            border-radius: 12px;
            padding: 30px;
        }
        
        [data-testid="stFileUploader"]:hover {
            border-color: rgba(0, 255, 0, 0.5);
            background: rgba(0, 30, 0, 0.4);
        }
        
        /* Sidebar */
        [data-testid="stSidebar"] {
            background: rgba(0, 0, 0, 0.95);
            backdrop-filter: blur(20px);
            border-right: 1px solid rgba(0, 255, 0, 0.15);
        }
        
        [data-testid="stSidebar"] [data-testid="stMarkdownContainer"] p {
            color: #a0a0a0 !important;
        }
        
        /* Slider */
        .stSlider > div > div > div {
            background: #00ff00;
        }
        
        .stSlider > div > div > div > div {
            color: #00ff00;
        }
        
        /* Success/Info boxes */
        .stSuccess {
            background: rgba(0, 100, 0, 0.2);
            border: 1px solid rgba(0, 255, 0, 0.3);
            border-radius: 8px;
            backdrop-filter: blur(10px);
            color: #00ff00 !important;
        }
        
        .stInfo {
            background: rgba(0, 100, 200, 0.15);
            border: 1px solid rgba(0, 150, 255, 0.3);
            border-radius: 8px;
            backdrop-filter: blur(10px);
            color: #00aaff !important;
        }
        
        .stWarning {
            background: rgba(200, 100, 0, 0.15);
            border: 1px solid rgba(255, 150, 0, 0.3);
            border-radius: 8px;
            backdrop-filter: blur(10px);
            color: #ffaa00 !important;
        }
        
        /* Tables */
        .dataframe {
            background: rgba(0, 20, 0, 0.3) !important;
            backdrop-filter: blur(10px);
            border: 1px solid rgba(0, 255, 0, 0.15);
            border-radius: 8px;
        }
        
        .dataframe th {
            background: rgba(0, 40, 0, 0.5) !important;
            color: #00ff00 !important;
            font-weight: 600 !important;
            text-transform: uppercase;
            font-size: 0.75rem;
            letter-spacing: 0.5px;
            padding: 12px !important;
        }
        
        .dataframe td {
            color: #c0c0c0 !important;
            padding: 10px !important;
            border-bottom: 1px solid rgba(0, 255, 0, 0.1) !important;
        }
        
        /* Input fields */
        input, textarea, select {
            background: rgba(0, 20, 0, 0.3) !important;
            border: 1px solid rgba(0, 255, 0, 0.2) !important;
            color: #ffffff !important;
            border-radius: 8px !important;
            backdrop-filter: blur(10px);
        }
        
        input:focus, textarea:focus, select:focus {
            border-color: rgba(0, 255, 0, 0.5) !important;
            box-shadow: 0 0 0 2px rgba(0, 255, 0, 0.1) !important;
        }
        
        /* Download button */
        .stDownloadButton>button {
            background: rgba(0, 100, 0, 0.4);
            color: #00ff00;
            border: 1px solid rgba(0, 255, 0, 0.4);
            border-radius: 8px;
            padding: 12px 28px;
            font-weight: 600;
            backdrop-filter: blur(10px);
            transition: all 0.3s;
        }
        
        .stDownloadButton>button:hover {
            background: rgba(0, 150, 0, 0.5);
            border-color: rgba(0, 255, 0, 0.6);
            box-shadow: 0 4px 16px rgba(0, 255, 0, 0.3);
        }
        
        /* Horizontal rule */
        hr {
            border-color: rgba(0, 255, 0, 0.1) !important;
            margin: 2rem 0;
        }
        
        /* Spinner */
        .stSpinner > div {
            border-top-color: #00ff00 !important;
        }
        
        /* Remove Streamlit branding */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        
        /* Scrollbar */
        ::-webkit-scrollbar {
            width: 10px;
            height: 10px;
        }
        
        ::-webkit-scrollbar-track {
            background: rgba(0, 0, 0, 0.3);
        }
        
        ::-webkit-scrollbar-thumb {
            background: rgba(0, 255, 0, 0.3);
            border-radius: 5px;
        }
        
        ::-webkit-scrollbar-thumb:hover {
            background: rgba(0, 255, 0, 0.5);
        }
    </style>
    """
