import pytest
import datetime
from documents import Report
class TestReport():

    def test_display_all_properties(self, capsys):
        """Test that display() prints all object properties"""
        report = Report()
        report.title = "Q4 Sales Report"
        report.content = "Sales increased by 25%"
        report.metadata = {"department": "Sales", "quarter": "Q4"}
        report.sections = ["Executive Summary", "Analysis", "Conclusion"]
        report.author = "John Doe"
        report.date = datetime.datetime(2024, 12, 31, 10, 30, 0)
        report.data_points = [100, 125, 150, 175]

        # Call display
        report.display()
        
        # Capture the output
        captured = capsys.readouterr()
        
        # Verify all properties are displayed
        assert "Q4 Sales Report" in captured.out
        assert "Sales increased by 25%" in captured.out
        assert "Sales" in captured.out
        assert "Q4" in captured.out
        assert "Executive Summary" in captured.out
        assert "John Doe" in captured.out
        assert "2024-12-31" in captured.out
        assert "100" in captured.out
        assert "125" in captured.out

    def test_display_with_none_values(self, capsys):
        """Test display() handles None values gracefully"""
        report = Report()
        report.display()
        
        captured = capsys.readouterr()
        # Should not crash and should display something
        assert len(captured.out) > 0
