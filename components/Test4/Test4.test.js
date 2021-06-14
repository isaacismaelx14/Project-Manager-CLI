import React from "react";
import "@testing-library/jest-dom";
import { render } from "@testing-library/react";
import Test4 from "./";
describe("<Test4 />", () => {
  let component;
  beforeEach(() => {
    component = render(<Test4 />);
  });
  test("should render", () => {
    component.getByText("Test4");
  });
});