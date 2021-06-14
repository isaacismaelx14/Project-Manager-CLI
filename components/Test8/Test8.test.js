import React from "react";
import "@testing-library/jest-dom";
import { render } from "@testing-library/react";
import Test8 from "./";
describe("<Test8 />", () => {
  let component;
  beforeEach(() => {
    component = render(<Test8 />);
  });
  test("should render", () => {
    component.getByText("Test8");
  });
});