import React from "react";
import "@testing-library/jest-dom";
import { render } from "@testing-library/react";
import Test5 from "./";
describe("<Test5 />", () => {
  let component;
  beforeEach(() => {
    component = render(<Test5 />);
  });
  test("should render", () => {
    component.getByText("Test5");
  });
});