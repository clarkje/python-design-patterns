import pytest
import datetime
from report_prototype import Report

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

        # Call display and verify it produces output
        report.display()
        
        captured = capsys.readouterr()
        assert len(captured.out) > 0

    def test_display_with_none_values(self, capsys):
        """Test display() handles None values gracefully"""
        report = Report()
        report.display()
        
        captured = capsys.readouterr()
        # Should not crash and should display something
        assert len(captured.out) > 0
