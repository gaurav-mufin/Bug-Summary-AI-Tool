import os
import sys
import click
from dotenv import load_dotenv
from openai import OpenAI
from rich.console import Console
from rich.panel import Panel
from rich.markdown import Markdown
from rich.progress import Progress, SpinnerColumn, TextColumn

# Load environment variables
load_dotenv()

console = Console()

class BugAnalyzer:
    def __init__(self, api_key=None):
        self.api_key = api_key or os.getenv("OPENAI_API_KEY")
        if not self.api_key:
            raise ValueError("OpenAI API Key not found. Please set OPENAI_API_KEY in .env file.")
        self.client = OpenAI(api_key=self.api_key)

    def analyze(self, bug_report: str):
        prompt = f"""
        You are an expert software engineer and debugger. 
        Analyze the following bug report or error log and provide a structured summary.
        
        Input:
        {bug_report}
        
        Output format (Markdown):
        # 🧠 Bug Analysis Report
        
        ## 📝 Summary
        [A concise 1-2 sentence summary of the issue]
        
        ## 🔍 Root Cause Analysis
        [Identify the most probable cause based on the logs/description]
        
        ## 🛠 Suggested Fixes
        - [Fix 1]
        - [Fix 2]
        
        ## 🧪 Debugging Steps
        1. [Step 1]
        2. [Step 2]
        """
        
        response = self.client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are a helpful assistant specialized in software debugging."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.2
        )
        
        return response.choices[0].message.content

@click.group()
def cli():
    """🧠 Bug Summary AI Tool - Analyze bug reports with AI."""
    pass

@cli.command()
@click.argument('file_path', type=click.Path(exists=True))
def analyze(file_path):
    """Analyze a bug report from a file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        analyzer = BugAnalyzer()
        
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            transient=True,
        ) as progress:
            progress.add_task(description="Analyzing bug report...", total=None)
            result = analyzer.analyze(content)
        
        console.print(Panel(Markdown(result), title="Analysis Results", border_style="green"))
        
    except Exception as e:
        console.print(f"[bold red]Error:[/bold red] {str(e)}")

@cli.command()
def test():
    """Run a quick test to verify API connectivity."""
    try:
        analyzer = BugAnalyzer()
        console.print("[yellow]Verifying API connectivity...[/yellow]")
        analyzer.client.models.list()
        console.print("[bold green]Success![/bold green] API key is valid.")
    except Exception as e:
        console.print(f"[bold red]Failed:[/bold red] {str(e)}")

if __name__ == "__main__":
    if len(sys.argv) == 1:
        # If no arguments, show help
        cli.main(args=['--help'])
    else:
        cli()